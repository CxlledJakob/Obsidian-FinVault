"""Shared paths and helpers for the local PDF pilot.

Writes are allowed only under Trading/Pilot. Trading/Notes and the PDF inbox
are never write targets.
"""

from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

PIPELINE_DIR = Path(__file__).resolve().parent
PILOT_DIR = PIPELINE_DIR.parent
TRADING_DIR = PILOT_DIR.parent
DATA_DIR = PILOT_DIR / "data"
NOTES_DIR = PILOT_DIR / "notes"
CHECKPOINT_DIR = DATA_DIR / "checkpoints"

PDF_DIR = TRADING_DIR / "Inbox" / "Pilot_Py"
TAXONOMY_TXT = TRADING_DIR / "Research" / "Taxonomie" / "Themenstruktur.txt"
TAXONOMY_JSON = DATA_DIR / "taxonomy.json"
PAGES_JSONL = DATA_DIR / "pages.jsonl"
CHUNKS_JSONL = DATA_DIR / "chunks.jsonl"
BLOCKS_JSONL = DATA_DIR / "blocks.jsonl"
BLOCKS_META = DATA_DIR / "blocks_meta.json"

FORBIDDEN_DIRS = (
    TRADING_DIR / "Notes",
    TRADING_DIR / "Inbox",
    TRADING_DIR / "Books",
    TRADING_DIR / "Research",
    TRADING_DIR / "Templates",
)

BLOCK_TYPES = (
    "definition",
    "mechanism",
    "rule",
    "evidence",
    "number",
    "exception",
    "method",
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


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict) -> None:
    ensure_parent(path)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


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


def load_taxonomy(path: Path | None = None) -> dict:
    payload = read_json(path or TAXONOMY_JSON)
    by_id = {topic["id"]: topic for topic in payload["topics"]}
    payload["by_id"] = by_id
    payload["id_set"] = set(by_id) | {"unassigned"}
    return payload


def filter_topics(raw, allowed: set[str]) -> list[str]:
    if isinstance(raw, str):
        raw = [raw]
    if not isinstance(raw, list):
        raw = []
    kept: list[str] = []
    for item in raw:
        topic_id = str(item).strip()
        if topic_id in allowed and topic_id not in kept:
            kept.append(topic_id)
    real = [topic_id for topic_id in kept if topic_id != "unassigned"]
    return real or ["unassigned"]


def page_windows(page_count: int, size: int = WINDOW_PAGES, overlap: int = WINDOW_OVERLAP) -> list[tuple[int, int]]:
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
            break
        start += step
    return windows


def chapter_ranges(toc: list, page_count: int) -> list[dict] | None:
    """One range per chapter bookmark. None when the outline is too thin to use."""
    entries = []
    for row in toc or []:
        if len(row) < 3:
            continue
        level, title, page = int(row[0]), str(row[1]).strip(), int(row[2])
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
        ranges.append({"title": "Front matter", "start": 1, "end": deduped[0][1] - 1, "kind": "front"})
    for index, (title, page) in enumerate(deduped):
        end = deduped[index + 1][1] - 1 if index + 1 < len(deduped) else page_count
        if end < page:
            end = page
        ranges.append({"title": title, "start": page, "end": end, "kind": "chapter"})
    return ranges


def normalize_block_text(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def dedupe_key(text: str) -> str:
    return normalize_block_text(text).casefold()


# English phrases that may justify a German Begriff. Bare words like "trend"
# are intentionally absent so one sentence cannot be stamped onto a whole group.
LABEL_ANCHORS = {
    "Marktstruktur": ["market structure"],
    "Balance": ["balanced market", "market balance"],
    "Imbalance": ["imbalance"],
    "Akzeptanz": ["acceptance"],
    "Ablehnung": ["rejection"],
    "Preisfindung": ["price discovery"],
    "Rotation": ["rotation"],
    "Initiative Activity": ["initiative activity", "initiative buying", "initiative selling"],
    "Responsive Activity": ["responsive activity", "responsive buying", "responsive selling"],
    "Auction Market Theory": ["auction market"],
    "Excess": ["excess"],
    "Failed Auction": ["failed auction"],
    "Strukturbruch": ["break of structure", "structure break"],
    "Trendfortsetzung": ["trend continuation"],
    "Trendrichtung": ["trend direction"],
    "Trenddauer": ["trend duration", "duration of the trend", "duration of a trend"],
    "Aufwärtstrend": ["uptrend", "upward trend"],
    "Abwärtstrend": ["downtrend", "downward trend"],
    "Unterstützung": ["support level", "support zone"],
    "Widerstand": ["resistance level", "resistance zone"],
    "Handelsvolumen": ["trading volume"],
    "Point of Control": ["point of control"],
    "Value Area High": ["value area high"],
    "Value Area Low": ["value area low"],
    "Volume Profile": ["volume profile"],
}

ATTRIBUTION_RE = re.compile(
    r"pioneered by|this book|earlier book|steidlmayer|steenbarger|mind over markets|markets in profile",
    re.IGNORECASE,
)


def _flat(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "").casefold())


def topic_anchors(topic: dict) -> list[str]:
    if topic.get("level") != "begriff":
        return []
    label = topic.get("begriff") or ""
    anchors = list(LABEL_ANCHORS.get(label, []))
    # Single English words such as Balance or Expansion occur in ordinary prose.
    # Only a multi-word label is specific enough to anchor a topic by itself.
    if label and " " in label and len(label) >= 10 and not re.search(r"[äöüÄÖÜß]", label):
        anchors.append(label)
    unique = []
    for anchor in anchors:
        if anchor and anchor not in unique and len(anchor) >= 6:
            unique.append(anchor)
    unique.sort(key=len, reverse=True)
    return unique


def anchor_hit(text: str, anchors: list[str]) -> str | None:
    hay = _flat(text)
    for anchor in anchors:
        needle = _flat(anchor)
        if len(needle) < 6:
            continue
        if re.search(rf"(?<!\w){re.escape(needle)}(?!\w)", hay):
            return needle
    return None


def is_attribution(text: str) -> bool:
    return bool(ATTRIBUTION_RE.search(text or ""))


def echoed_label_count(text: str, source: str, tax: dict) -> int:
    count = 0
    for topic in tax["topics"]:
        if topic.get("level") != "begriff":
            continue
        label = topic.get("begriff") or ""
        if len(label) < 8 or re.search(r"[äöüÄÖÜß]", label):
            continue
        if anchor_hit(text, [label]) and not anchor_hit(source, [label]):
            count += 1
    return count


def select_topics(text: str, source: str, proposed: list[str], tax: dict, limit: int = 2) -> list[str]:
    """Keep a Begriff only when its own phrase is in the statement and on the page."""
    if is_attribution(text):
        return ["unassigned"]
    by_id = tax["by_id"]
    scored: list[tuple[int, str]] = []
    for topic_id in proposed:
        if topic_id == "unassigned":
            continue
        topic = by_id.get(topic_id)
        if not topic:
            continue
        anchors = topic_anchors(topic)
        in_text = anchor_hit(text, anchors)
        in_source = anchor_hit(source, anchors)
        if in_text and in_source:
            scored.append((len(in_text), topic_id))
    scored.sort(reverse=True)
    kept: list[str] = []
    for _length, topic_id in scored:
        if topic_id not in kept:
            kept.append(topic_id)
        if len(kept) >= limit:
            break
    return kept or ["unassigned"]


def topics_for_statement(text: str, source: str, proposed: list[str], tax: dict, limit: int = 1) -> list[str]:
    """Model ids are kept only when the phrase is present. Otherwise one matching phrase may be used."""
    chosen = select_topics(text, source, proposed, tax, limit=limit)
    if chosen != ["unassigned"]:
        return chosen
    hits: list[tuple[int, str]] = []
    for topic in candidates_in_source(tax, source, limit=12):
        hit = anchor_hit(text, topic_anchors(topic))
        if hit:
            hits.append((len(hit), topic["id"]))
    hits.sort(reverse=True)
    kept: list[str] = []
    for _length, topic_id in hits:
        if topic_id not in kept:
            kept.append(topic_id)
        if len(kept) >= limit:
            break
    return kept or ["unassigned"]


def candidates_in_source(tax: dict, source: str, limit: int = 12) -> list[dict]:
    found: list[tuple[int, dict]] = []
    for topic in tax["topics"]:
        if topic.get("level") != "begriff":
            continue
        hit = anchor_hit(source, topic_anchors(topic))
        if hit:
            found.append((len(hit), topic))
    found.sort(key=lambda item: item[0], reverse=True)
    rows = []
    seen = set()
    for _length, topic in found:
        if topic["id"] in seen:
            continue
        seen.add(topic["id"])
        rows.append(topic)
        if len(rows) >= limit:
            break
    return rows
