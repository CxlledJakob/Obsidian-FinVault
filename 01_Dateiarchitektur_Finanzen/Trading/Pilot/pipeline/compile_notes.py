"""Group blocks by topic id into Pilot notes.

Identical text on the same topic is merged. A non-empty conflicts list is
written as CONFLICT. Haupt notes only list their Unterthemen. Nothing is
written under Trading/Notes.
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

from common import (
    BLOCKS_JSONL,
    BLOCKS_META,
    BLOCK_TYPES,
    NOTES_DIR,
    PAGES_JSONL,
    PILOT_DIR,
    TRADING_DIR,
    dedupe_key,
    echoed_label_count,
    is_attribution,
    iter_jsonl,
    load_taxonomy,
    normalize_block_text,
    topics_for_statement,
    slug,
)

VAULT = TRADING_DIR.parents[1]
TODAY = date.today().isoformat()


def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def vault_link(path: Path, label: str) -> str:
    rel = path.resolve().relative_to(VAULT.resolve()).as_posix()
    return f"[[{rel}|{label.replace('|', '/')}]]"


def clear_generated(notes_dir: Path) -> None:
    if not notes_dir.exists():
        return
    for path in notes_dir.rglob("*.md"):
        head = path.read_text(encoding="utf-8")[:400]
        if "generator: pilot-pipeline" in head:
            path.unlink()
    for path in sorted(notes_dir.rglob("*"), reverse=True):
        if path.is_dir() and not any(path.iterdir()):
            path.rmdir()


def load_blocks() -> list[dict]:
    blocks = []
    for record in iter_jsonl(BLOCKS_JSONL):
        if record.get("_invalid"):
            continue
        blocks.append(record)
    return blocks


def page_index() -> dict[tuple[str, int], str]:
    pages = {}
    for record in iter_jsonl(PAGES_JSONL):
        if record.get("_invalid"):
            continue
        pages[(record["file"], int(record["page"]))] = record.get("text") or ""
    return pages


def retag_blocks(blocks: list[dict], tax: dict) -> list[dict]:
    """Drop copied definitions. One definition sentence belongs to one Unterthema."""
    pages = page_index()
    owners: dict[str, str] = {}
    cleaned = []
    for block in blocks:
        src = (block.get("src") or [{}])[0]
        source = pages.get((src.get("file"), int(src.get("page") or 0)), "")
        text = block.get("text") or ""
        if is_attribution(text) or echoed_label_count(text, source, tax) >= 2:
            continue
        topics = topics_for_statement(text, source, block.get("topics") or [], tax, limit=1 if block.get("type") == "definition" else 2)
        if block.get("type") == "definition":
            real = [topic_id for topic_id in topics if topic_id != "unassigned"]
            key = dedupe_key(text)
            if real:
                if key in owners and owners[key] != real[0]:
                    topics = ["unassigned"]
                else:
                    owners[key] = real[0]
                    topics = [real[0]]
        updated = dict(block)
        updated["topics"] = topics
        cleaned.append(updated)
    return cleaned


def merge_blocks(blocks: list[dict]) -> list[dict]:
    merged: list[dict] = []
    index: dict[str, int] = {}
    for block in blocks:
        key = dedupe_key(block.get("text") or "")
        if key in index:
            target = merged[index[key]]
            seen_src = {(item["file"], item["page"]) for item in target["src"]}
            for item in block.get("src") or []:
                pair = (item["file"], item["page"])
                if pair not in seen_src:
                    target["src"].append({"file": item["file"], "page": item["page"]})
                    seen_src.add(pair)
            for ref in block.get("conflicts") or []:
                if ref not in target["conflicts"] and ref != target["id"]:
                    target["conflicts"].append(ref)
            continue
        index[key] = len(merged)
        merged.append(
            {
                "id": block["id"],
                "type": block.get("type") or "mechanism",
                "topics": list(block.get("topics") or ["unassigned"]),
                "src": [{"file": item["file"], "page": item["page"]} for item in block.get("src") or []],
                "text": normalize_block_text(block.get("text") or ""),
                "conflicts": [ref for ref in (block.get("conflicts") or []) if ref != block["id"]],
                "origin": block.get("origin") or "",
            }
        )
    return merged


def format_src(block: dict) -> str:
    parts = []
    for item in block["src"]:
        parts.append(f"{item['file']}:{item['page']}")
    return ", ".join(parts)


def render_lines(blocks: list[dict]) -> str:
    by_type: dict[str, list[dict]] = defaultdict(list)
    for block in merge_blocks(blocks):
        block_type = block["type"] if block["type"] in BLOCK_TYPES else "mechanism"
        by_type[block_type].append(block)
    sections = []
    for block_type in BLOCK_TYPES:
        rows = by_type.get(block_type) or []
        if not rows:
            continue
        lines = [f"## {block_type}"]
        for block in rows:
            text = block["text"].replace("|", "/")
            if block["conflicts"]:
                conflict = ", ".join(block["conflicts"])
                lines.append(f"- {block['id']} | CONFLICT {conflict} | {text} | {format_src(block)}")
            else:
                lines.append(f"- {block['id']} | {text} | {format_src(block)}")
        sections.append("\n".join(lines))
    return "\n\n".join(sections) + ("\n" if sections else "")


def write_note(path: Path, frontmatter: str, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if PILOT_DIR.resolve() not in path.resolve().parents:
        raise SystemExit(f"refusing to write outside Pilot: {path}")
    path.write_text(frontmatter + "\n" + body, encoding="utf-8")


def self_test() -> None:
    sample = [
        {
            "id": "b1",
            "type": "rule",
            "topics": ["01/preisbildung/marktstruktur"],
            "src": [{"file": "a.pdf", "page": 1}],
            "text": "Same claim.",
            "conflicts": [],
        },
        {
            "id": "b2",
            "type": "rule",
            "topics": ["01/preisbildung/marktstruktur"],
            "src": [{"file": "a.pdf", "page": 2}],
            "text": "Same claim.",
            "conflicts": [],
        },
        {
            "id": "b3",
            "type": "rule",
            "topics": ["01/preisbildung/marktstruktur"],
            "src": [{"file": "a.pdf", "page": 3}],
            "text": "Other claim.",
            "conflicts": ["b4"],
        },
        {
            "id": "b4",
            "type": "rule",
            "topics": ["01/preisbildung/marktstruktur"],
            "src": [{"file": "a.pdf", "page": 4}],
            "text": "Opposite claim.",
            "conflicts": ["b3"],
        },
    ]
    rendered = render_lines(sample)
    assert rendered.count("Same claim.") == 1, rendered
    assert "a.pdf:1" in rendered and "a.pdf:2" in rendered
    assert "CONFLICT b4" in rendered and "CONFLICT b3" in rendered
    print("compile_notes self-test ok")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return

    tax = load_taxonomy()
    blocks = retag_blocks(load_blocks(), tax)
    clear_generated(NOTES_DIR)
    NOTES_DIR.mkdir(parents=True, exist_ok=True)

    by_topic: dict[str, list[dict]] = defaultdict(list)
    for block in blocks:
        topics = block.get("topics") or ["unassigned"]
        for topic_id in topics:
            by_topic[topic_id].append(block)

    haupts = [topic for topic in tax["topics"] if topic["level"] == "haupt"]
    groups = [topic for topic in tax["topics"] if topic["level"] == "gruppe"]
    begriffe = [topic for topic in tax["topics"] if topic["level"] == "begriff"]

    haupt_paths: dict[str, Path] = {}
    for haupt in haupts:
        haupt_paths[haupt["id"]] = NOTES_DIR / f"{haupt['id']}-{slug(haupt['haupt'])}.md"

    begriff_paths: dict[str, Path] = {}
    for topic in begriffe:
        if not by_topic.get(topic["id"]):
            continue
        folder = NOTES_DIR / f"{topic['haupt_id']}-{slug(topic['haupt'])}"
        path = folder / f"{slug(topic['gruppe'])}--{slug(topic['begriff'])}.md"
        begriff_paths[topic["id"]] = path
        files = sorted({item["file"] for block in by_topic[topic["id"]] for item in block.get("src") or []})
        quellen = "\n".join(f"  - {yaml_quote(name)}" for name in files) or "  []"
        origins = sorted({block.get("origin") or "" for block in by_topic[topic["id"]]})
        merged = merge_blocks(by_topic[topic["id"]])
        front = "\n".join(
            [
                "---",
                "typ: wissen",
                "status: entwurf",
                f"hauptthema: {yaml_quote(topic['haupt'])}",
                f"unterthema: {yaml_quote(topic['begriff'])}",
                f"priorität: {topic['priority']}",
                "quellen:",
                quellen,
                f"erstellt: {TODAY}",
                f"aktualisiert: {TODAY}",
                "generator: pilot-pipeline",
                "---",
                "",
            ]
        )
        body = (
            f"# {topic['begriff']}\n\n"
            f"id: `{topic['id']}` | gruppe: {topic['gruppe']} | priorität: {topic['priority']}\n\n"
            f"units: {len(merged)} | sources: {len(files)} | origin: {', '.join(origins)}\n\n"
            + render_lines(by_topic[topic["id"]])
        )
        write_note(path, front, body)

    index_rows = []
    for haupt in haupts:
        haupt_blocks = []
        child_notes = []
        lines = []
        current_group = None
        for group in groups:
            if group["haupt_id"] != haupt["id"]:
                continue
            lines.append(f"## {group['gruppe']}")
            group_items = [topic for topic in begriffe if topic["gruppe_id"] == group["id"]]
            if not group_items:
                lines.append("- (keine Begriffe)")
                continue
            for topic in group_items:
                count = len(by_topic.get(topic["id"]) or [])
                if count:
                    link = vault_link(begriff_paths[topic["id"]], topic["begriff"])
                    lines.append(f"- {topic['begriff']} ({topic['priority']}) — {count} — {link}")
                    child_notes.append(topic["id"])
                    haupt_blocks.extend(by_topic[topic["id"]])
                else:
                    lines.append(f"- {topic['begriff']} ({topic['priority']}) — 0")
            current_group = group
        haupt_only = []
        for block in by_topic.get(haupt["id"]) or []:
            specific = False
            for topic_id in block.get("topics") or []:
                topic = tax["by_id"].get(topic_id)
                if topic and topic["level"] == "begriff" and topic["haupt_id"] == haupt["id"]:
                    specific = True
            if not specific:
                haupt_only.append(block)
        if haupt_only:
            lines.append("## Nur Hauptebene")
            lines.append(render_lines(haupt_only).rstrip())
        front = "\n".join(
            [
                "---",
                "typ: übersicht",
                "status: entwurf",
                f"hauptthema: {yaml_quote(haupt['haupt'])}",
                f"erstellt: {TODAY}",
                f"aktualisiert: {TODAY}",
                "generator: pilot-pipeline",
                "---",
                "",
            ]
        )
        body = f"# {haupt['id']} {haupt['haupt']}\n\nDieser Index listet nur die Unterthemen.\n\n" + "\n".join(lines) + "\n"
        write_note(haupt_paths[haupt["id"]], front, body)
        index_rows.append((haupt, len({block["id"] for block in haupt_blocks}), len(child_notes)))
        _ = current_group

    if by_topic.get("unassigned"):
        path = NOTES_DIR / "unassigned.md"
        merged = merge_blocks(by_topic["unassigned"])
        front = "\n".join(
            [
                "---",
                "typ: wissen",
                "status: entwurf",
                "hauptthema: \"unassigned\"",
                f"erstellt: {TODAY}",
                f"aktualisiert: {TODAY}",
                "generator: pilot-pipeline",
                "---",
                "",
            ]
        )
        body = f"# unassigned\n\nunits: {len(merged)}\n\n" + render_lines(by_topic["unassigned"])
        write_note(path, front, body)

    meta = {}
    if BLOCKS_META.exists():
        import json

        meta = json.loads(BLOCKS_META.read_text(encoding="utf-8"))
    runs = meta.get("runs") if isinstance(meta.get("runs"), list) else []
    if not runs and meta.get("chunk_id"):
        runs = [meta]
    if runs:
        herkunft = "; ".join(
            f"{item.get('origin') or 'unbekannt'} {item.get('model') or ''} {item.get('chunk_id') or ''} Seiten {item.get('start')}-{item.get('end')}".strip()
            for item in runs
        )
    else:
        herkunft = "unbekannt"
    header = "\n".join(
        [
            "---",
            "typ: übersicht",
            "status: entwurf",
            f"erstellt: {TODAY}",
            f"aktualisiert: {TODAY}",
            "generator: pilot-pipeline",
            "---",
            "",
            "# Pilotindex — 25 Hauptthemen",
            "",
            f"Herkunft: {herkunft}",
            "",
        ]
    )
    lines = []
    for haupt, block_count, note_count in index_rows:
        link = vault_link(haupt_paths[haupt["id"]], haupt["haupt"])
        lines.append(f"- {haupt['id']} {link} — Bausteine: {block_count} — Unterthemen mit Notiz: {note_count}")
    index_path = NOTES_DIR / "index.md"
    write_note(index_path, header, "\n".join(lines) + "\n")
    print(f"notes={NOTES_DIR}")
    print(f"haupt_files={len(haupt_paths)} begriff_files={len(begriff_paths)} blocks={len(blocks)}")


if __name__ == "__main__":
    main()
