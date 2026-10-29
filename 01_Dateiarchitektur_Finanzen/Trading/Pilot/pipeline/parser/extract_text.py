#!/usr/bin/env python3
"""Extract every PDF page to pages.jsonl and write chapter or window chunks.

Bookmarks become one chunk per chapter. Without an outline, chunks are 20
pages with a 1-page overlap. A PDF with no text layer is skipped. Pages are
read with PyMuPDF only. Checkpoints are the pages already stored, so a rerun
continues.
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path

import pymupdf

from common import (
    CHUNKS_JSONL,
    DATA_DIR,
    PDF_DIR,
    PAGES_JSONL,
    PILOT_DIR,
    TRADING_DIR,
    WINDOW_OVERLAP,
    WINDOW_PAGES,
    append_jsonl,
    chapter_ranges,
    file_key,
    iter_jsonl,
    page_windows,
    rewrite_jsonl,
    write_json,
)

MIN_LAYER_CHARS = 400


def clean_text(text: str) -> str:
    import re

    text = text.replace("\x00", "").replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"([A-Za-z])-\s+([a-z])", r"\1\2", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def text_layer_sample(document) -> tuple[int, int]:
    count = document.page_count
    if count <= 0:
        return (0, 0)
    step = max(1, count // 20)
    indexes = list(range(0, count, step))
    if count - 1 not in indexes:
        indexes.append(count - 1)
    total = 0
    for index in indexes:
        total += len((document[index].get_text("text") or "").strip())
    return total, len(indexes)


def existing_pages(path: Path) -> tuple[dict[tuple[str, int], dict], int]:
    kept: dict[tuple[str, int], dict] = {}
    invalid = 0
    duplicates = 0
    for record in iter_jsonl(path):
        if record.get("_invalid"):
            invalid += 1
            continue
        key = (record["file"], int(record["page"]))
        if key in kept:
            duplicates += 1
        kept[key] = record
    if invalid or duplicates:
        rewrite_jsonl(path, list(kept.values()))
    return kept, invalid + duplicates


def build_chunks(pdf_path: Path, page_count: int, toc: list) -> list[dict]:
    key = file_key(pdf_path.name)
    ranges = chapter_ranges(toc, page_count)
    chunks: list[dict] = []
    if ranges:
        for index, item in enumerate(ranges, 1):
            chunks.append(
                {
                    "id": f"{key}-c{index:02d}",
                    "key": key,
                    "file": pdf_path.name,
                    "kind": item["kind"],
                    "title": item["title"],
                    "start": item["start"],
                    "end": item["end"],
                }
            )
        return chunks
    for index, (start, end) in enumerate(
        page_windows(page_count, WINDOW_PAGES, WINDOW_OVERLAP), 1
    ):
        chunks.append(
            {
                "id": f"{key}-w{index:02d}",
                "key": key,
                "file": pdf_path.name,
                "kind": "window",
                "title": f"pages {start}-{end}",
                "start": start,
                "end": end,
            }
        )
    return chunks


def extract_page(page) -> str:
    return clean_text(page.get_text("text") or "")


def snapshot_outside_pilot() -> None:
    """Remember mtimes outside Pilot so a later check can see we did not touch the vault notes."""
    snap = DATA_DIR / "outside_mtime.json"
    if snap.exists():
        return
    rows = []
    for path in TRADING_DIR.rglob("*"):
        if not path.is_file():
            continue
        if path == PILOT_DIR or PILOT_DIR in path.parents:
            continue
        stat = path.stat()
        rows.append(
            {"path": str(path), "mtime_ns": stat.st_mtime_ns, "size": stat.st_size}
        )
    write_json(snap, {"files": rows})


def self_test() -> None:
    assert page_windows(20) == [(1, 20)]
    assert page_windows(21) == [(1, 20), (20, 21)]
    assert page_windows(40) == [(1, 20), (20, 39), (39, 40)]
    assert page_windows(585)[-1] == (571, 585)
    assert page_windows(585)[1] == (20, 39)
    toc = [
        (1, "Book", 1),
        (2, "Chapter 1", 5),
        (2, "Chapter 2", 10),
        (2, "Chapter 3", 12),
        (3, "Section", 6),
    ]
    ranges = chapter_ranges(toc, 15)
    assert ranges is not None
    assert ranges[0]["title"] == "Book" or ranges[0]["start"] == 1
    assert any(item["title"] == "Chapter 1" and item["end"] == 9 for item in ranges)
    assert any(item["title"] == "Chapter 3" and item["end"] == 15 for item in ranges)
    assert chapter_ranges([], 10) is None
    print("extract_text self-test ok")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--pdf-dir", default=str(PDF_DIR))
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return

    snapshot_outside_pilot()
    pdf_dir = Path(args.pdf_dir)
    pdfs = sorted(pdf_dir.glob("*.pdf"))
    if not pdfs:
        raise SystemExit(f"no PDFs in {pdf_dir}")

    all_chunks: list[dict] = []
    skipped: list[dict] = []
    usable: list[Path] = []
    for pdf_path in pdfs:
        document = pymupdf.open(pdf_path)
        try:
            sampled, sample_pages = text_layer_sample(document)
            if sampled < MIN_LAYER_CHARS:
                skipped.append(
                    {
                        "file": pdf_path.name,
                        "key": file_key(pdf_path.name),
                        "pdf_pages": document.page_count,
                        "reason": "no text layer",
                        "sampled_chars": sampled,
                        "sample_pages": sample_pages,
                    }
                )
                print(
                    f"SKIP {file_key(pdf_path.name)} no text layer pdf_pages="
                    f"{document.page_count} sampled_chars={sampled}",
                    flush=True,
                )
                continue
            usable.append(pdf_path)
            all_chunks.extend(
                build_chunks(pdf_path, document.page_count, document.get_toc())
            )
        finally:
            document.close()

    if not usable:
        raise SystemExit("no PDF has a text layer")

    keep_files = {path.name for path in usable}
    write_json(DATA_DIR / "skipped_pdfs.json", {"files": skipped})
    write_json(
        DATA_DIR / "chunks_meta.json",
        {"chunk_count": len(all_chunks), "skipped": len(skipped)},
    )
    rewrite_jsonl(CHUNKS_JSONL, all_chunks)

    done, repaired = existing_pages(PAGES_JSONL)
    dropped = [
        (file_name, page)
        for file_name, page in done
        if file_name not in keep_files or done[(file_name, page)].get("method") != "pymupdf"
    ]
    if dropped:
        rewrite_jsonl(
            PAGES_JSONL,
            [
                record
                for (file_name, _page), record in done.items()
                if file_name in keep_files and record.get("method") == "pymupdf"
            ],
        )
        done = {
            (file_name, page): record
            for (file_name, page), record in done.items()
            if file_name in keep_files and record.get("method") == "pymupdf"
        }
        repaired += len(dropped)

    summary = []
    for pdf_path in usable:
        document = pymupdf.open(pdf_path)
        try:
            name = pdf_path.name
            methods: dict[str, int] = defaultdict(int)
            written = 0
            for index in range(document.page_count):
                page_no = index + 1
                if (name, page_no) in done:
                    methods["skipped"] += 1
                    continue
                text = extract_page(document[index])
                method = "pymupdf"
                record = {
                    "file": name,
                    "key": file_key(name),
                    "page": page_no,
                    "chars": len(text),
                    "method": method,
                    "text": text,
                }
                append_jsonl(PAGES_JSONL, record)
                done[(name, page_no)] = record
                methods[method] += 1
                written += 1
                if written == 1 or page_no % 25 == 0 or page_no == document.page_count:
                    print(
                        f"{file_key(name)} page {page_no}/{document.page_count}"
                        f" method={method} chars={len(text)}",
                        flush=True,
                    )
            present = {page for file_name, page in done if file_name == name}
            expected = set(range(1, document.page_count + 1))
            missing = sorted(expected - present)
            if missing:
                raise SystemExit(f"{name} missing pages: {missing[:8]}")
            summary.append(
                {
                    "file": name,
                    "key": file_key(name),
                    "pdf_pages": document.page_count,
                    "stored_pages": len(present),
                    "methods": dict(methods),
                }
            )
        finally:
            document.close()

    write_json(
        DATA_DIR / "text_summary.json",
        {
            "repaired_records": repaired,
            "files": summary,
            "chunks": len(all_chunks),
            "skipped": skipped,
        },
    )
    print(f"pages={PAGES_JSONL}")
    print(f"chunks={CHUNKS_JSONL} count={len(all_chunks)}")
    for item in summary:
        print(
            f"{item['key']} pdf_pages={item['pdf_pages']}"
            f" stored={item['stored_pages']} methods={item['methods']}"
        )


if __name__ == "__main__":
    main()
