"""Check page counts, closed topic ids, and that notes stayed under Pilot."""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import pymupdf

from common import (
    BLOCKS_JSONL,
    BLOCKS_META,
    DATA_DIR,
    NOTES_DIR,
    PDF_DIR,
    PAGES_JSONL,
    PILOT_DIR,
    file_key,
    iter_jsonl,
    load_taxonomy,
)

CONDITION = re.compile(r"\b(if|when|unless|only|above|below|before|after|wenn|nur|falls|ausser|außer)\b", re.I)


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    failures = []
    tax = load_taxonomy()
    allowed = tax["id_set"]

    pages = defaultdict(dict)
    methods = defaultdict(lambda: defaultdict(int))
    chars = defaultdict(int)
    duplicates = 0
    for record in iter_jsonl(PAGES_JSONL):
        if record.get("_invalid"):
            failures.append("invalid line in pages.jsonl")
            continue
        key = (record["file"], int(record["page"]))
        if key in pages[record["file"]]:
            duplicates += 1
        pages[record["file"]][int(record["page"])] = record
        methods[record["file"]][record.get("method") or ""] += 1
        chars[record["file"]] += int(record.get("chars") or 0)
    if duplicates:
        failures.append(f"duplicate pages: {duplicates}")

    skipped_path = DATA_DIR / "skipped_pdfs.json"
    skipped_names = set()
    if skipped_path.exists():
        skipped_names = {item["file"] for item in json.loads(skipped_path.read_text(encoding="utf-8")).get("files", [])}
    pdfs = sorted(Path(PDF_DIR).glob("*.pdf"))
    page_report = []
    for pdf_path in pdfs:
        document = pymupdf.open(pdf_path)
        try:
            expected = document.page_count
        finally:
            document.close()
        stored = pages.get(pdf_path.name, {})
        if pdf_path.name in skipped_names:
            match = len(stored) == 0
            if not match:
                failures.append(f"skipped PDF still has stored pages: {file_key(pdf_path.name)}")
        else:
            missing = [number for number in range(1, expected + 1) if number not in stored]
            extra = [number for number in stored if number < 1 or number > expected]
            match = not missing and not extra and len(stored) == expected
            if not match:
                failures.append(f"page count mismatch {file_key(pdf_path.name)} pdf={expected} stored={len(stored)} missing={missing[:5]}")
        page_report.append(
            {
                "key": file_key(pdf_path.name),
                "pdf_pages": expected,
                "stored_pages": len(stored),
                "match": match,
                "chars": chars[pdf_path.name],
                "methods": dict(methods[pdf_path.name]),
            }
        )

    blocks = [record for record in iter_jsonl(BLOCKS_JSONL) if not record.get("_invalid")]
    if not blocks:
        failures.append("no blocks")
    bad_topics = []
    origins = defaultdict(int)
    for block in blocks:
        origins[block.get("origin") or ""] += 1
        for topic_id in block.get("topics") or []:
            if topic_id not in allowed:
                bad_topics.append(topic_id)
        if "id" not in block or "type" not in block or "text" not in block or "conflicts" not in block or "src" not in block:
            failures.append(f"block missing fields: {block.get('id')}")
    if bad_topics:
        failures.append(f"topic ids outside taxonomy: {sorted(set(bad_topics))[:8]}")

    markdown = list(NOTES_DIR.rglob("*.md")) if NOTES_DIR.exists() else []
    if not markdown:
        failures.append("no markdown under Pilot/notes")
    outside = [str(path) for path in markdown if PILOT_DIR.resolve() not in path.resolve().parents and path.resolve() != PILOT_DIR]
    if outside:
        failures.append(f"markdown outside Pilot: {outside[:3]}")
    haupt_notes = [path for path in markdown if path.parent == NOTES_DIR and re.match(r"\d\d-", path.name)]
    if len(haupt_notes) != 25:
        failures.append(f"expected 25 haupt notes, found {len(haupt_notes)}")
    if not (NOTES_DIR / "index.md").exists():
        failures.append("missing notes/index.md")

    sample = None
    for block in blocks:
        if re.search(r"\d", block.get("text") or "") and CONDITION.search(block.get("text") or ""):
            sample = block
            break
    sample_report = {"found": False}
    if sample is None:
        failures.append("no block kept both a number and a condition")
    else:
        page = int(sample["src"][0]["page"])
        file_name = sample["src"][0]["file"]
        source = pages[file_name][page]["text"]
        numbers = re.findall(r"\d+(?:[.,]\d+)?", sample["text"])
        missing_numbers = [number for number in numbers if number not in source]
        condition = CONDITION.search(sample["text"]).group(0)
        sample_report = {
            "found": True,
            "block_id": sample["id"],
            "page": page,
            "number": numbers[0] if numbers else None,
            "condition_word": condition,
            "number_on_page": not missing_numbers,
        }
        if missing_numbers:
            failures.append(f"sample number missing on source page: {missing_numbers[:4]}")

    snap_path = DATA_DIR / "outside_mtime.json"
    changed = []
    if snap_path.exists():
        snap = json.loads(snap_path.read_text(encoding="utf-8"))
        for row in snap["files"]:
            path = Path(row["path"])
            if not path.exists():
                changed.append(f"missing {path.name}")
                continue
            stat = path.stat()
            if stat.st_size != row["size"] or stat.st_mtime_ns != row["mtime_ns"]:
                changed.append(str(path))
        if changed:
            failures.append(f"files outside Pilot changed: {changed[:8]}")
    else:
        failures.append("missing outside_mtime snapshot")

    meta = {}
    if BLOCKS_META.exists():
        meta = json.loads(BLOCKS_META.read_text(encoding="utf-8"))

    for file_name, page_map in pages.items():
        if file_name in skipped_names:
            failures.append(f"pages stored for skipped PDF: {file_key(file_name)}")
        for record in page_map.values():
            if record.get("method") != "pymupdf":
                failures.append(f"non-text-layer method: {record.get('method')}")
                break

    report = {
        "ok": not failures,
        "failures": failures,
        "pages": page_report,
        "blocks": len(blocks),
        "origins": dict(origins),
        "meta": meta,
        "markdown_files": len(markdown),
        "sample": sample_report,
        "notes_dir": str(NOTES_DIR),
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
