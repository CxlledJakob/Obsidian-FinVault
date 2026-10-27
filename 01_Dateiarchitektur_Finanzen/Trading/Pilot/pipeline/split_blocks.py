#!/usr/bin/env python3
"""Split Pilot text markdown into ~8-page block files for downstream processing."""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

PILOT_ROOT = Path(__file__).resolve().parent.parent
TEXT_DIR = PILOT_ROOT / "text"
BLOCKS_DIR = PILOT_ROOT / "blocks"

PAGES_PER_BLOCK = 8
PAGE_MARKER_RE = re.compile(r"^--- page (\d+) ---\s*$", re.MULTILINE)
# Skip chunks with almost no body text (after removing markers and whitespace).
MIN_SUBSTANTIVE_CHARS = 40

BOOKS = (
    ("markets-in-profile.md", "markets-in-profile"),
    ("mind-over-markets.md", "mind-over-markets"),
)


def strip_frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 3)
    if end == -1:
        return text
    return text[end + 4 :].lstrip("\n")


def book_title(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "Untitled"


def parse_pages(body: str) -> list[tuple[int, str]]:
    matches = list(PAGE_MARKER_RE.finditer(body))
    pages: list[tuple[int, str]] = []
    for i, match in enumerate(matches):
        page_num = int(match.group(1))
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        pages.append((page_num, body[start:end].rstrip() + "\n"))
    return pages


def substantive_length(chunk_text: str) -> int:
    without_markers = PAGE_MARKER_RE.sub("", chunk_text)
    collapsed = re.sub(r"\s+", "", without_markers)
    return len(collapsed)


def write_block(
    out_dir: Path,
    slug: str,
    title: str,
    start_page: int,
    end_page: int,
    block_index: int,
    page_chunks: list[str],
) -> Path:
    filename = f"{slug}-block-{block_index:03d}-p{start_page:03d}-p{end_page:03d}.md"
    path = out_dir / filename
    header = (
        f"# {title}\n\n"
        f"**Pages:** {start_page}–{end_page}\n\n"
    )
    path.write_text(header + "".join(page_chunks), encoding="utf-8")
    return path


def split_book(source_name: str, slug: str) -> list[Path]:
    source_path = TEXT_DIR / source_name
    if not source_path.is_file():
        raise FileNotFoundError(source_path)

    raw = source_path.read_text(encoding="utf-8")
    title = book_title(raw)
    pages = parse_pages(strip_frontmatter(raw))
    if not pages:
        raise ValueError(f"No page markers found in {source_path}")

    out_dir = BLOCKS_DIR / slug
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    written: list[Path] = []
    block_index = 0
    for offset in range(0, len(pages), PAGES_PER_BLOCK):
        group = pages[offset : offset + PAGES_PER_BLOCK]
        body = "".join(chunk for _, chunk in group)
        if substantive_length(body) < MIN_SUBSTANTIVE_CHARS:
            continue
        block_index += 1
        start_page = group[0][0]
        end_page = group[-1][0]
        written.append(
            write_block(out_dir, slug, title, start_page, end_page, block_index, [c for _, c in group])
        )
    return written


def main() -> int:
    counts: dict[str, int] = {}
    for source_name, slug in BOOKS:
        paths = split_book(source_name, slug)
        counts[slug] = len(paths)
        print(f"{slug}: wrote {len(paths)} block file(s) -> {BLOCKS_DIR / slug}")

    if any(n == 0 for n in counts.values()):
        print("error: at least one book produced no blocks", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
