#!/usr/bin/env python3
"""Split Pilot text markdown into chapter-aware block files for downstream processing."""

from __future__ import annotations

import re
import shutil
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path

PILOT_ROOT = Path(__file__).resolve().parent.parent
TEXT_DIR = PILOT_ROOT / "text"
BLOCKS_DIR = PILOT_ROOT / "blocks"

MAX_PAGES_PER_BLOCK = 20
PAGE_OVERLAP = 1
PAGE_MARKER_RE = re.compile(r"^--- page (\d+) ---\s*$", re.MULTILINE)
CHAPTER_BODY_RE = re.compile(r"^C H A P T E R (\d+)\s*$", re.MULTILINE)
CHAPTER_TOC_RE = re.compile(r"^CHAPTER (\d+)\s*$")
MIN_SUBSTANTIVE_CHARS = 40

RUNNING_HEADERS = frozenset(
    {
        "MARKETS IN PROFILE",
        "MIND OVER MARKETS",
        "PREFACE",
        "CONTENTS",
        "ACKNOWLEDGMENTS",
        "INDEX",
        "APPENDIX A: MARKET UPDATE",
        "ABOUT THE AUTHORS",
    }
)

BOOKS = (
    ("markets-in-profile.md", "markets-in-profile"),
    ("mind-over-markets.md", "mind-over-markets"),
)


@dataclass(frozen=True)
class Chapter:
    number: int
    title: str
    start_page: int
    end_page: int


@dataclass(frozen=True)
class BlockSpec:
    chapter: Chapter | None
    subchapter: str | None
    start_page: int
    end_page: int


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


def pages_by_number(pages: list[tuple[int, str]]) -> dict[int, str]:
    return {num: chunk for num, chunk in pages}


def substantive_length(chunk_text: str) -> int:
    without_markers = PAGE_MARKER_RE.sub("", chunk_text)
    collapsed = re.sub(r"\s+", "", without_markers)
    return len(collapsed)


def normalize_heading(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"\s+", " ", text.strip())
    return text


def norm_key(text: str) -> str:
    return re.sub(r"[^A-Z0-9]", "", normalize_heading(text).upper())


def line_is_mostly_uppercase(line: str) -> bool:
    letters = [c for c in line if c.isalpha()]
    if len(letters) < 4:
        return False
    upper = sum(1 for c in letters if c.isupper())
    return upper / len(letters) >= 0.9


def is_section_heading(line: str) -> bool:
    line = normalize_heading(line)
    if len(line) < 8 or len(line) > 120:
        return False
    if line.isdigit():
        return False
    if not line_is_mostly_uppercase(line):
        return False
    if line.upper() in RUNNING_HEADERS:
        return False
    if re.match(r"^(FIGURE|TABLE|CHAPTER)\b", line, re.I):
        return False
    if re.fullmatch(r"[A-Z0-9 .,'\"()?\-–—/]+", line) is None:
        return False
    words = [w for w in re.split(r"\s+", line) if w]
    if len(words) < 2 and len(line) < 18:
        return False
    return True


def is_chapter_title_line(line: str) -> bool:
    line = normalize_heading(line)
    if not line or line.isdigit():
        return False
    if re.match(r'^["“‘—\-–]', line):
        return False
    if len(line) == 1 and line.isalpha():
        return False
    if len(line) > 55:
        return False
    if len(line.split()) > 10:
        return False
    lowercase = sum(1 for c in line if c.isalpha() and c.islower())
    if any(ch in line for ch in ",;") and lowercase > 3:
        return False
    if re.search(r"[.!?]", line) and lowercase > 4:
        return False
    return True


def is_preface_page(chunk: str) -> bool:
    return bool(
        re.search(r"^P\s*R\s*E\s*F\s*A\s*C\s*E\s*$", chunk, re.MULTILINE)
        or re.search(r"^Preface\s*$", chunk, re.MULTILINE)
    )


def toc_end_page(pages: list[tuple[int, str]], first_chapter_page: int) -> int:
    for page_num, chunk in pages:
        if page_num >= first_chapter_page:
            return page_num - 1
        if is_preface_page(chunk):
            return page_num - 1
    return first_chapter_page - 1


def parse_toc_subchapters(
    pages: list[tuple[int, str]], first_chapter_page: int
) -> dict[int, list[str]]:
    toc_lines: list[str] = []
    started = False
    end_page = toc_end_page(pages, first_chapter_page)
    for page_num, chunk in pages:
        if page_num > end_page:
            break
        if re.search(r"\bContents\b", chunk, re.I):
            started = True
        if not started:
            continue
        for raw in chunk.splitlines():
            line = raw.strip()
            if line and not line.startswith("--- page"):
                toc_lines.append(line)

    result: dict[int, list[str]] = {}
    current: int | None = None
    index = 0
    skip_titles = frozenset(
        {"preface", "acknowledgments", "index", "about the authors"}
    )
    while index < len(toc_lines):
        line = toc_lines[index]
        match = CHAPTER_TOC_RE.match(line)
        if match:
            current = int(match.group(1))
            result.setdefault(current, [])
            index += 1
            while index < len(toc_lines) and not toc_lines[index].isdigit():
                index += 1
            if index < len(toc_lines) and toc_lines[index].isdigit():
                index += 1
            continue
        if current is None or line.isdigit() or CHAPTER_TOC_RE.match(line):
            index += 1
            continue
        title = line
        index += 1
        while (
            index < len(toc_lines)
            and not toc_lines[index].isdigit()
            and not CHAPTER_TOC_RE.match(toc_lines[index])
        ):
            title = f"{title} {toc_lines[index]}"
            index += 1
        normalized = normalize_heading(title)
        lowered = normalized.lower()
        if lowered not in skip_titles and not lowered.startswith("appendix"):
            result[current].append(normalized)
        if index < len(toc_lines) and toc_lines[index].isdigit():
            index += 1
    return result


def heading_matches_toc(line: str, toc_titles: list[str]) -> bool:
    line_key = norm_key(line)
    if len(line_key) < 8:
        return False
    for title in toc_titles:
        title_key = norm_key(title)
        if len(title_key) < 8:
            continue
        if line_key == title_key or title_key in line_key or line_key in title_key:
            return True
    return False


def collect_heading_lines(lines: list[str], start_index: int) -> tuple[str, int]:
    parts: list[str] = []
    i = start_index
    while i < len(lines):
        line = normalize_heading(lines[i])
        if not line:
            i += 1
            continue
        if PAGE_MARKER_RE.match(line):
            break
        if CHAPTER_BODY_RE.match(line):
            break
        if line.isdigit():
            i += 1
            continue
        if not line_is_mostly_uppercase(line):
            break
        if not is_section_heading(line) and not parts:
            break
        if not line_is_mostly_uppercase(line):
            break
        parts.append(line)
        i += 1
        if len(parts) >= 4:
            break
    return normalize_heading(" ".join(parts)), i


def extract_chapter_title(page_text: str) -> str:
    lines = page_text.splitlines()
    for i, raw in enumerate(lines):
        if not CHAPTER_BODY_RE.match(raw.strip()):
            continue
        parts: list[str] = []
        for line in lines[i + 1 :]:
            line = normalize_heading(line)
            if not line:
                if parts:
                    break
                continue
            if PAGE_MARKER_RE.match(line):
                break
            if line.isdigit():
                continue
            if not is_chapter_title_line(line):
                break
            parts.append(line)
            if len(parts) >= 4:
                break
        return normalize_heading(" ".join(parts))
    return ""


def find_chapters(pages: list[tuple[int, str]]) -> list[Chapter]:
    ordered_nums = [num for num, _ in pages]
    starts: list[tuple[int, int, str]] = []
    for page_num, chunk in pages:
        match = CHAPTER_BODY_RE.search(chunk)
        if match:
            number = int(match.group(1))
            title = extract_chapter_title(chunk) or f"Chapter {number}"
            starts.append((number, page_num, title))

    if not starts:
        return []

    max_page = ordered_nums[-1]
    chapters: list[Chapter] = []
    for i, (number, start_page, title) in enumerate(starts):
        end_page = starts[i + 1][1] - 1 if i + 1 < len(starts) else max_page
        chapters.append(Chapter(number, title, start_page, end_page))
    return chapters


def find_subchapter_split_pages(
    chapter: Chapter, toc_titles: list[str], pages: list[tuple[int, str]]
) -> dict[int, str]:
    if not toc_titles:
        return {}
    title_key = norm_key(chapter.title)
    split_pages: dict[int, str] = {}
    for page_num, chunk in pages:
        if page_num <= chapter.start_page or page_num > chapter.end_page:
            continue
        past_chapter_marker = page_num != chapter.start_page
        lines = chunk.splitlines()
        for index, raw in enumerate(lines):
            line = normalize_heading(raw)
            if PAGE_MARKER_RE.match(line):
                continue
            if CHAPTER_BODY_RE.match(line):
                past_chapter_marker = True
                continue
            if not past_chapter_marker:
                continue
            heading, _ = collect_heading_lines(lines, index)
            candidate = heading if heading and is_section_heading(heading) else line
            if not is_section_heading(candidate):
                continue
            if norm_key(candidate) == title_key:
                continue
            if not heading_matches_toc(candidate, toc_titles):
                continue
            split_pages.setdefault(page_num, heading or candidate)
            break
    return split_pages


def page_windows(start_page: int, end_page: int) -> list[tuple[int, int]]:
    if start_page > end_page:
        return []
    page_nums = list(range(start_page, end_page + 1))
    if len(page_nums) <= MAX_PAGES_PER_BLOCK:
        return [(start_page, end_page)]
    windows: list[tuple[int, int]] = []
    index = 0
    while index < len(page_nums):
        window = page_nums[index : index + MAX_PAGES_PER_BLOCK]
        windows.append((window[0], window[-1]))
        if window[-1] == end_page:
            break
        index += MAX_PAGES_PER_BLOCK - PAGE_OVERLAP
    return windows


def split_range_clean(
    chapter: Chapter | None,
    subchapter: str | None,
    start_page: int,
    end_page: int,
    pages: list[tuple[int, str]],
    subchapters_by_page: dict[int, str] | None = None,
) -> list[BlockSpec]:
    length = end_page - start_page + 1
    if length <= MAX_PAGES_PER_BLOCK:
        return [BlockSpec(chapter, subchapter, start_page, end_page)]

    if chapter is not None and subchapters_by_page:
        split_pages = sorted(
            page for page in subchapters_by_page if start_page < page <= end_page
        )
        if split_pages:
            specs: list[BlockSpec] = []
            boundaries = [start_page] + split_pages
            for i, boundary in enumerate(boundaries):
                seg_end = (
                    boundaries[i + 1] - 1 if i + 1 < len(boundaries) else end_page
                )
                seg_sub = (
                    subchapter
                    if i == 0
                    else subchapters_by_page.get(boundary)
                )
                child_specs = split_range_clean(
                    chapter,
                    seg_sub,
                    boundary,
                    seg_end,
                    pages,
                    subchapters_by_page=None,
                )
                specs.extend(child_specs)
            return specs

    return [
        BlockSpec(chapter, subchapter, win_start, win_end)
        for win_start, win_end in page_windows(start_page, end_page)
    ]


def build_block_specs(pages: list[tuple[int, str]]) -> list[BlockSpec]:
    chapters = find_chapters(pages)
    if not chapters:
        return [
            BlockSpec(None, None, start, end)
            for start, end in page_windows(pages[0][0], pages[-1][0])
        ]

    toc_by_chapter = parse_toc_subchapters(pages, chapters[0].start_page)
    specs: list[BlockSpec] = []
    first_chapter_page = chapters[0].start_page
    if pages[0][0] < first_chapter_page:
        preamble = Chapter(0, "Front matter", pages[0][0], first_chapter_page - 1)
        specs.extend(
            split_range_clean(
                preamble,
                None,
                preamble.start_page,
                preamble.end_page,
                pages,
                None,
            )
        )

    for chapter in chapters:
        chapter_length = chapter.end_page - chapter.start_page + 1
        sub_map: dict[int, str] | None = None
        if chapter_length > MAX_PAGES_PER_BLOCK:
            sub_map = find_subchapter_split_pages(
                chapter, toc_by_chapter.get(chapter.number, []), pages
            )
            if not sub_map:
                sub_map = None
        specs.extend(
            split_range_clean(
                chapter,
                None,
                chapter.start_page,
                chapter.end_page,
                pages,
                sub_map,
            )
        )
    return specs


def format_block_heading(
    book: str, spec: BlockSpec
) -> str:
    page_range = f"pages {spec.start_page}–{spec.end_page}"
    if spec.chapter is None:
        return f"# {book} — {page_range}\n\n"
    if spec.chapter.number == 0:
        return f"# {book} — Front matter ({page_range})\n\n"
    chapter_label = (
        f"Chapter {spec.chapter.number}: {spec.chapter.title}"
    )
    if spec.subchapter:
        return (
            f"# {book} — {chapter_label} — {spec.subchapter} ({page_range})\n\n"
        )
    return f"# {book} — {chapter_label} ({page_range})\n\n"


def write_block(
    out_dir: Path,
    slug: str,
    book: str,
    spec: BlockSpec,
    block_index: int,
    page_map: dict[int, str],
) -> Path:
    filename = (
        f"{slug}-block-{block_index:03d}-p{spec.start_page:03d}-p{spec.end_page:03d}.md"
    )
    path = out_dir / filename
    chunks = [page_map[page] for page in range(spec.start_page, spec.end_page + 1)]
    path.write_text(
        format_block_heading(book, spec) + "".join(chunks),
        encoding="utf-8",
    )
    return path


def looks_like_fixed_eight_page_slices(paths: list[Path]) -> bool:
    if len(paths) < 5:
        return False
    eight = 0
    for path in paths:
        match = re.search(r"-p(\d+)-p(\d+)\.md$", path.name)
        if not match:
            continue
        start_page, end_page = int(match.group(1)), int(match.group(2))
        if end_page - start_page + 1 == 8:
            eight += 1
    return eight >= max(5, int(len(paths) * 0.75))


def split_book(source_name: str, slug: str) -> list[Path]:
    source_path = TEXT_DIR / source_name
    if not source_path.is_file():
        raise FileNotFoundError(source_path)

    raw = source_path.read_text(encoding="utf-8")
    title = book_title(raw)
    pages = parse_pages(strip_frontmatter(raw))
    if not pages:
        raise ValueError(f"No page markers found in {source_path}")

    page_map = pages_by_number(pages)
    specs = build_block_specs(pages)

    out_dir = BLOCKS_DIR / slug
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    written: list[Path] = []
    block_index = 0
    for spec in specs:
        body = "".join(
            page_map[page] for page in range(spec.start_page, spec.end_page + 1)
        )
        if substantive_length(body) < MIN_SUBSTANTIVE_CHARS:
            continue
        block_index += 1
        written.append(
            write_block(out_dir, slug, title, spec, block_index, page_map)
        )
    return written


def main() -> int:
    counts: dict[str, int] = {}
    for source_name, slug in BOOKS:
        paths = split_book(source_name, slug)
        counts[slug] = len(paths)
        print(f"{slug}: wrote {len(paths)} block file(s) -> {BLOCKS_DIR / slug}")
        if paths:
            sample = paths[min(1, len(paths) - 1)]
            first_line = sample.read_text(encoding="utf-8").splitlines()[0]
            print(f"  sample: {sample.name}")
            print(f"  heading: {first_line}")

    if any(n == 0 for n in counts.values()):
        print("error: at least one book produced no blocks", file=sys.stderr)
        return 1

    for source_name, slug in BOOKS:
        paths = list((BLOCKS_DIR / slug).glob("*.md"))
        if looks_like_fixed_eight_page_slices(paths):
            print(
                f"error: {slug} still looks like fixed 8-page slices",
                file=sys.stderr,
            )
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
