"""Paths and helpers for the PDF parser.

Writes stay under Trading/Pilot. Trading/Notes and the book folders are not
write targets.
"""

from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

PILOT_DIR = Path(__file__).resolve().parents[2]
TRADING_DIR = PILOT_DIR.parent
DATA_DIR = PILOT_DIR / "data"
PDF_DIR = TRADING_DIR / "Books"
PAGES_JSONL = DATA_DIR / "pages.jsonl"
CHUNKS_JSONL = DATA_DIR / "chunks.jsonl"

FORBIDDEN_DIRS = (
    TRADING_DIR / "Notes",
    TRADING_DIR / "Inbox",
    TRADING_DIR / "Books",
    TRADING_DIR / "Research",
    TRADING_DIR / "Templates",
)

WINDOW_PAGES = 20
WINDOW_OVERLAP = 1


def assert_pilot_write(path: Path) -> Path:
    resolved = path.resolve()
    pilot = PILOT_DIR.resolve()
    if resolved != pilot and pilot not in resolved.parents:
        raise SystemExit(f"refusing to write outside Trading/Pilot: {resolved}")
    for forbidden in FORBIDDEN_DIRS:
        root = forbidden.resolve()
        if resolved == root or root in resolved.parents:
            raise SystemExit(f"refusing to write into {root}")
    return resolved


def ensure_parent(path: Path) -> Path:
    assert_pilot_write(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def slug(value: str) -> str:
    text = value.strip().lower()
    text = (
        text.replace("ä", "ae")
        .replace("ö", "oe")
        .replace("ü", "ue")
        .replace("ß", "ss")
    )
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "x"


def file_key(filename: str) -> str:
    name = filename.lower()
    if name.startswith("technical analysis"):
        return "murphy"
    if name.startswith("mind over markets"):
        return "mom"
    if name.startswith("markets in profile"):
        return "mip"
    return slug(filename)[:32]


def write_json(path: Path, payload: dict) -> None:
    ensure_parent(path)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def iter_jsonl(path: Path):
    if not path.exists():
        return
    with path.open(encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            raw = line.strip()
            if not raw:
                continue
            try:
                yield json.loads(raw)
            except json.JSONDecodeError:
                yield {"_invalid": True, "_line": line_no}


def append_jsonl(path: Path, record: dict) -> None:
    ensure_parent(path)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")
        handle.flush()


def rewrite_jsonl(path: Path, records: list[dict]) -> None:
    ensure_parent(path)
    temp = path.with_suffix(path.suffix + ".tmp")
    assert_pilot_write(temp)
    with temp.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    temp.replace(path)


def page_windows(
    page_count: int,
    size: int = WINDOW_PAGES,
    overlap: int = WINDOW_OVERLAP,
) -> list[tuple[int, int]]:
    """1-based inclusive windows. The next window starts on the last page of the previous one."""
    if page_count <= 0:
        return []
    if page_count <= size:
        return [(1, page_count)]
    step = size - overlap
    if step < 1:
        raise ValueError("overlap must be smaller than window size")
    windows: list[tuple[int, int]] = []
    start = 1
    while True:
        end = min(start + size - 1, page_count)
        windows.append((start, end))
        if end >= page_count:
            return windows
        start += step


def chapter_ranges(toc: list, page_count: int) -> list[dict] | None:
    """One range per chapter bookmark. None when the outline is too thin to use."""
    entries: list[tuple[int, str, int]] = []
    for row in toc or []:
        if len(row) < 3:
            continue
        level = int(row[0])
        title = str(row[1]).strip()
        page = int(row[2])
        if page < 1 or page > page_count or not title:
            continue
        entries.append((level, title, page))
    if len(entries) < 3:
        return None
    counts: dict[int, int] = {}
    for level, _title, _page in entries:
        counts[level] = counts.get(level, 0) + 1
    chosen = None
    for level in sorted(counts):
        if counts[level] >= 3:
            chosen = level
            break
    if chosen is None:
        return None
    selected = [(title, page) for level, title, page in entries if level == chosen]
    selected.sort(key=lambda item: item[1])
    deduped: list[tuple[str, int]] = []
    for title, page in selected:
        if deduped and deduped[-1][1] == page:
            continue
        deduped.append((title, page))
    if len(deduped) < 3:
        return None
    ranges: list[dict] = []
    if deduped[0][1] > 1:
        ranges.append(
            {
                "title": "Front matter",
                "start": 1,
                "end": deduped[0][1] - 1,
                "kind": "front",
            }
        )
    for index, (title, page) in enumerate(deduped):
        if index + 1 < len(deduped):
            end = deduped[index + 1][1] - 1
        else:
            end = page_count
        if end < page:
            end = page
        ranges.append(
            {"title": title, "start": page, "end": end, "kind": "chapter"}
        )
    return ranges
