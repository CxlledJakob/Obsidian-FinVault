"""Turn one text chunk into blocks.

Ollama is used when the local daemon already has a model. Topic ids that are
not in taxonomy.json become unassigned. If no local model is available, a
deterministic fallback covers only the first short chapter or the first 20
pages of one PDF and marks every block fallback_unreviewed.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

from common import (
    BLOCKS_JSONL,
    BLOCKS_META,
    BLOCK_TYPES,
    CHECKPOINT_DIR,
    CHUNKS_JSONL,
    PAGES_JSONL,
    append_jsonl,
    candidates_in_source,
    dedupe_key,
    echoed_label_count,
    file_key,
    filter_topics,
    is_attribution,
    iter_jsonl,
    load_taxonomy,
    normalize_block_text,
    rewrite_jsonl,
    select_topics,
    topics_for_statement,
    write_json,
)

MODEL = "qwen2.5:3b-instruct-q4_K_M"
OLLAMA_CHAT = "http://127.0.0.1:11434/api/chat"
OLLAMA_TAGS = "http://127.0.0.1:11434/api/tags"

# Hints only choose which closed taxonomy branches are shown to the model.
HAUPT_HINTS = {
    "01": ["price action", "swing high", "swing low", "higher high", "auction", "market structure", "imbalance"],
    "02": ["trendline", "trend line", "dow theory", "uptrend", "downtrend", "channel"],
    "03": ["support", "resistance", "breakout", "retest"],
    "04": ["head and shoulders", "double top", "double bottom", "triangle", "flag", "pennant", "wedge"],
    "05": ["candlestick", "doji", "hammer", "engulfing", "shooting star"],
    "06": ["volume", "on-balance volume", "obv"],
    "07": ["bid", "ask", "order book", "spread", "liquidity"],
    "08": ["order block", "fair value gap", "liquidity sweep"],
    "09": ["wyckoff", "selling climax", "upthrust"],
    "10": ["elliott", "impulse wave", "zigzag"],
    "11": ["moving average", "macd", "rsi", "stochastic", "bollinger", "oscillator"],
    "12": ["momentum", "divergence"],
    "13": ["volatility", "average true range", " atr"],
    "14": ["bull market", "bear market", "seasonal"],
    "15": ["intermarket", "yield curve", "sector rotation"],
    "16": ["standard deviation", "regression"],
    "17": ["drawdown", "stop loss", "stop-loss", "risk"],
    "18": ["position size", "position sizing", "risk/reward"],
    "19": ["psychology", "discipline", "emotion"],
    "20": ["sharpe", "profit factor", "equity curve"],
    "21": ["backtest", "trading system"],
    "22": ["anomaly", "january effect"],
    "23": ["intrinsic value", "fundamental"],
    "24": ["inflation", "interest rate", "federal reserve"],
    "25": ["price/earnings", "earnings per share"],
}

LABEL_ALIASES = {
    "breakout": "Breakout",
    "support": "Unterstützung",
    "resistance": "Widerstand",
    "moving average": "Simple Moving Average",
    "dow theory": "Dow-Theorie",
    "head and shoulders": "Schulter-Kopf-Schulter",
    "double top": "Doppeltop",
    "double bottom": "Doppelboden",
    "doji": "Doji",
    "hammer": "Hammer",
    "bollinger": "Bollinger Bands",
    "relative strength index": "Relative Strength Index",
    "point of control": "Point of Control",
    "auction market": "Auction Market Theory",
}


def ollama_ready() -> bool:
    try:
        with urllib.request.urlopen(OLLAMA_TAGS, timeout=5) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except Exception:
        return False
    names = [item.get("name", "") for item in payload.get("models", [])]
    return any(name == MODEL or name.split(":")[0] == MODEL.split(":")[0] and MODEL in name for name in names)


def ollama_chat(messages: list[dict], num_ctx: int, num_predict: int) -> tuple[str, str]:
    body = {
        "model": MODEL,
        "messages": messages,
        "stream": False,
        "format": "json",
        "keep_alive": "30m",
        "options": {"temperature": 0, "num_ctx": num_ctx, "num_predict": num_predict, "seed": 1},
    }
    request = urllib.request.Request(
        OLLAMA_CHAT,
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=300) as response:
        payload = json.loads(response.read().decode("utf-8"))
    return payload.get("message", {}).get("content", ""), payload.get("done_reason", "")


def parse_model_json(raw: str) -> dict | list:
    text = raw.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?", "", text).strip()
        text = re.sub(r"```$", "", text).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        end = text.rfind("}")
        if end == -1:
            raise
        snippet = text[: end + 1]
        if '"blocks"' in snippet and not snippet.rstrip().endswith("]}"):
            snippet += "]}"
        try:
            return json.loads(snippet)
        except json.JSONDecodeError:
            match = re.search(r"(\{.*\}|\[.*\])", text, re.S)
            if not match:
                raise
            return json.loads(match.group(1))


def load_pages(filename: str) -> dict[int, str]:
    pages: dict[int, str] = {}
    for record in iter_jsonl(PAGES_JSONL):
        if record.get("_invalid"):
            continue
        if record.get("file") == filename:
            pages[int(record["page"])] = record.get("text") or ""
    return pages


def load_chunks() -> list[dict]:
    return [record for record in iter_jsonl(CHUNKS_JSONL) if not record.get("_invalid")]


def window_stats(pages: dict[int, str], start: int, end: int) -> tuple[int, float]:
    texts = [pages.get(page, "") for page in range(start, end + 1)]
    lines = [line.strip() for text in texts for line in text.splitlines() if line.strip()]
    total = sum(len(text) for text in texts)
    average = (sum(len(line) for line in lines) / len(lines)) if lines else 0.0
    return total, average


def select_body_chunk(chunks: list[dict], key: str) -> dict:
    """First window whose pages are long enough to be body text, not the title or contents."""
    chosen_file = next(chunk["file"] for chunk in chunks if chunk["key"] == key)
    pages = load_pages(chosen_file)
    best = None
    best_median = -1
    for chunk in chunks:
        if chunk["key"] != key or chunk["kind"] == "front":
            continue
        title = chunk["title"].casefold()
        if any(label in title for label in ("contents", "preface", "acknowledgment", "suggested reading", "about the author", "index")) and "chapter" not in title:
            continue
        lengths = sorted(len(pages.get(page, "")) for page in range(chunk["start"], chunk["end"] + 1))
        if not lengths:
            continue
        median = lengths[len(lengths) // 2]
        short = sum(1 for size in lengths if size < 400)
        if median > best_median:
            best = chunk
            best_median = median
        if median >= 1500 and short <= 1:
            return chunk
    if best is None:
        raise SystemExit(f"no chunk for {key}")
    return best


def print_chunk_table(chunks: list[dict], key: str, selected_id: str) -> None:
    chosen_file = next(chunk["file"] for chunk in chunks if chunk["key"] == key)
    pages = load_pages(chosen_file)
    for chunk in chunks:
        if chunk["key"] != key:
            continue
        total, average = window_stats(pages, chunk["start"], chunk["end"])
        mark = " selected" if chunk["id"] == selected_id else ""
        title = chunk["title"].replace("\n", " ")[:60]
        print(f"{chunk['id']} {chunk['start']}-{chunk['end']} chars={total} avg_line={average:.1f} {chunk['kind']} {title}{mark}")


def hint_haupts(text: str) -> list[str]:
    lowered = text.casefold()
    scored = []
    for haupt_id, phrases in HAUPT_HINTS.items():
        score = sum(lowered.count(phrase) for phrase in phrases)
        if score:
            scored.append((score, haupt_id))
    scored.sort(reverse=True)
    return [haupt_id for _score, haupt_id in scored[:4]]


def classify_haupts(excerpt: str, haupt_topics: list[dict]) -> list[str]:
    catalog = "\n".join(f"{topic['id']} {topic['haupt']}" for topic in haupt_topics)
    messages = [
        {
            "role": "system",
            "content": "Choose up to 4 topic ids that this trading text is about. Return JSON {\"ids\":[\"01\"]}. Use only ids from the list.",
        },
        {"role": "user", "content": f"Topics:\n{catalog}\n\nText:\n{excerpt[:1800]}"},
    ]
    raw, _reason = ollama_chat(messages, num_ctx=4096, num_predict=80)
    payload = parse_model_json(raw)
    ids = payload.get("ids", []) if isinstance(payload, dict) else []
    valid = {topic["id"] for topic in haupt_topics}
    chosen = []
    for item in ids:
        topic_id = str(item).strip()
        if topic_id in valid and topic_id not in chosen:
            chosen.append(topic_id)
        if len(chosen) >= 4:
            break
    return chosen


def candidate_terms(tax: dict, haupt_ids: list[str]) -> list[dict]:
    rows = [
        topic
        for topic in tax["topics"]
        if topic["level"] == "begriff" and topic["haupt_id"] in set(haupt_ids)
    ]
    rows.sort(key=lambda topic: ({"A": 0, "B": 1, "C": 2}.get(topic["priority"], 9), topic["id"]))
    if len(rows) > 80:
        rows = [topic for topic in rows if topic["priority"] in {"A", "B"}][:80]
    return rows


def slice_pairs(start: int, end: int, pages: dict[int, str]):
    page = start
    while page <= end:
        nxt = min(page + 1, end)
        blob = "\n".join(pages.get(number, "") for number in range(page, nxt + 1))
        if nxt > page and len(blob) > 9000:
            nxt = page
        yield page, nxt
        page = nxt + 1


def marked_excerpt(pages: dict[int, str], start: int, end: int) -> str:
    parts = []
    for page in range(start, end + 1):
        parts.append(f"[page {page}]\n{pages.get(page, '')}")
    return "\n\n".join(parts)


def grounded(text: str, source: str) -> bool:
    numbers = re.findall(r"\d+(?:[.,]\d+)?", text)
    source_numbers = set(re.findall(r"\d+(?:[.,]\d+)?", source))
    if any(number not in source_numbers for number in numbers):
        return False
    words = re.findall(r"[A-Za-z]{5,}", text)
    if len(words) < 4:
        return False
    lowered = source.casefold()
    hits = sum(1 for word in words if word.casefold() in lowered)
    return hits >= max(3, int(len(words) * 0.55))


def resolve_topic_token(token: str, candidates: list[dict], allowed: set[str]) -> str | None:
    cleaned = token.strip().strip("`\"'")
    if cleaned in allowed:
        return cleaned
    lowered = cleaned.casefold()
    label_hits = [topic["id"] for topic in candidates if topic.get("begriff") and topic["begriff"].casefold() == lowered]
    if len(label_hits) == 1:
        return label_hits[0]
    return None


def blocks_from_model(raw_blocks, pages, file_name, start, end, candidates, allowed, tax) -> list[dict]:
    source = "\n".join(pages.get(page, "") for page in range(start, end + 1))
    kept = []
    for item in raw_blocks:
        if not isinstance(item, dict):
            continue
        text = normalize_block_text(str(item.get("text") or ""))
        if len(text) < 40:
            continue
        if len(text) > 700:
            text = text[:700].rsplit(" ", 1)[0]
        if not grounded(text, source):
            continue
        block_type = str(item.get("type") or "mechanism").strip().lower()
        if block_type not in BLOCK_TYPES:
            block_type = "mechanism"
        if is_attribution(text) or echoed_label_count(text, source, tax) >= 2:
            continue
        tokens = item.get("topics") or []
        resolved = []
        for token in tokens if isinstance(tokens, list) else [tokens]:
            topic_id = resolve_topic_token(str(token), candidates, allowed)
            if topic_id and topic_id not in resolved:
                resolved.append(topic_id)
        topics = topics_for_statement(text, source, resolved, tax, limit=1 if block_type == "definition" else 2)
        try:
            page = int(item.get("page"))
        except (TypeError, ValueError):
            page = start
        if page < start or page > end:
            page = start
        conflicts = []
        for ref in item.get("conflicts") or []:
            if isinstance(ref, str) and ref.startswith("b-") and ref not in conflicts:
                conflicts.append(ref)
        kept.append(
            {
                "type": block_type,
                "topics": topics,
                "src": [{"file": file_name, "page": page}],
                "text": text,
                "conflicts": conflicts,
            }
        )
        if len(kept) >= 8:
            break
    return kept


def call_for_blocks(excerpt: str, catalog: str, page_from: int, page_to: int, fewer: bool) -> list:
    limit = 4 if fewer else 8
    messages = [
        {
            "role": "system",
            "content": (
                "Extract dense claims from a trading textbook. Return JSON "
                '{"blocks":[{"type":"definition|mechanism|rule|evidence|number|exception|method",'
                '"topics":["id"],"page":1,"text":"one claim","conflict_with":[]}]}. '
                "Each block is one statement. topics is one id, or [\"unassigned\"]. "
                "Use an id only when the statement is about that exact concept. "
                "Do not attach the same sentence to several ids. "
                "Do not name a concept that the source paragraph does not discuss. "
                "Keep every number and every condition (if, when, unless, only). "
                "Do not invent numbers. Do not translate. "
                f"At most {limit} blocks."
            ),
        },
        {
            "role": "user",
            "content": f"Allowed ids:\n{catalog}\n\nPages {page_from}-{page_to}:\n{excerpt}",
        },
    ]
    raw, reason = ollama_chat(messages, num_ctx=4096, num_predict=500 if fewer else 900)
    try:
        payload = parse_model_json(raw)
    except json.JSONDecodeError:
        if reason != "length":
            raise
        raise ValueError("truncated")
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for key in ("blocks", "bausteine", "items"):
            if isinstance(payload.get(key), list):
                return payload[key]
        if payload.get("text"):
            return [payload]
    return []


def assign_ids(blocks: list[dict], chunk_id: str, start: int) -> list[dict]:
    assigned = []
    for index, block in enumerate(blocks, 1):
        block_id = f"b-{chunk_id}-p{start}-{index:03d}"
        conflicts = [ref for ref in block.get("conflicts") or [] if ref != block_id]
        assigned.append(
            {
                "id": block_id,
                "type": block["type"],
                "topics": block["topics"],
                "src": block["src"],
                "text": block["text"],
                "conflicts": [item for item in conflicts if item != block_id],
            }
        )
    return assigned


def ollama_slice(pages, chunk, start, end, tax) -> list[dict]:
    excerpt = marked_excerpt(pages, start, end)
    source = "\n".join(pages.get(page, "") for page in range(start, end + 1))
    candidates = candidates_in_source(tax, source, limit=12)
    if candidates:
        catalog = "\n".join(f"{topic['id']} | {topic['priority']} | {topic['begriff']}" for topic in candidates)
    else:
        catalog = "(none; use unassigned)"
    raw_blocks = []
    last_error = None
    for fewer in (False, True):
        try:
            raw_blocks = call_for_blocks(excerpt, catalog, start, end, fewer)
            break
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, ValueError, KeyError) as exc:
            last_error = exc
            raw_blocks = []
    if last_error and not raw_blocks:
        error_path = CHECKPOINT_DIR / "last_model_error.txt"
        error_path.parent.mkdir(parents=True, exist_ok=True)
        error_path.write_text(f"{chunk['id']} {start}-{end} {type(last_error).__name__}\n", encoding="utf-8")
        raise SystemExit(f"Ollama failed on {chunk['id']} pages {start}-{end}: {type(last_error).__name__}")
    built = blocks_from_model(raw_blocks, pages, chunk["file"], start, end, candidates, tax["id_set"], tax)
    unique = []
    seen = set()
    for block in built:
        key = dedupe_key(block["text"])
        if key in seen:
            continue
        seen.add(key)
        unique.append(block)
    return assign_ids(unique, chunk["id"], start)


def match_fallback_topics(paragraph: str, tax: dict) -> list[str]:
    lowered = paragraph.casefold()
    hits = []
    by_label: dict[str, list[str]] = {}
    for topic in tax["topics"]:
        if topic["level"] != "begriff":
            continue
        by_label.setdefault(topic["begriff"].casefold(), []).append(topic["id"])
        label = topic["begriff"]
        if len(label) >= 6 and label.casefold() in lowered and topic["id"] not in hits:
            hits.append(topic["id"])
    for phrase, label in LABEL_ALIASES.items():
        if re.search(rf"\b{re.escape(phrase)}\b", lowered):
            for topic_id in by_label.get(label.casefold(), []):
                if topic_id not in hits:
                    hits.append(topic_id)
    return filter_topics(hits[:5], tax["id_set"])


def guess_type(paragraph: str) -> str:
    lowered = paragraph.casefold()
    if any(token in lowered for token in ("defined as", "is defined", "definition of")):
        return "definition"
    if any(token in lowered for token in ("unless", "except when", "only if", "only when")):
        return "exception"
    if re.search(r"\d", paragraph) and any(token in lowered for token in ("percent", "%", "day", "week", "ratio")):
        return "number"
    if any(token in lowered for token in ("must ", "should ", " if ", " when ")):
        return "rule"
    return "mechanism"


def fallback_blocks_from_text(text: str, file_name: str, page: int, tax: dict) -> list[dict]:
    paragraphs = [normalize_block_text(part) for part in re.split(r"\n\s*\n", text)]
    paragraphs = [part for part in paragraphs if len(part) >= 140]
    paragraphs.sort(key=lambda part: (0 if re.search(r"\d", part) else 1, -len(part)))
    blocks = []
    for paragraph in paragraphs[:20]:
        blocks.append(
            {
                "type": guess_type(paragraph),
                "topics": match_fallback_topics(paragraph, tax),
                "src": [{"file": file_name, "page": page}],
                "text": paragraph[:700],
                "conflicts": [],
                "origin": "fallback_unreviewed",
            }
        )
    if not blocks and text.strip():
        blocks.append(
            {
                "type": "mechanism",
                "topics": ["unassigned"],
                "src": [{"file": file_name, "page": page}],
                "text": normalize_block_text(text)[:700],
                "conflicts": [],
                "origin": "fallback_unreviewed",
            }
        )
    return blocks


def fallback_span(chunks: list[dict], key: str) -> dict:
    file_chunks = [chunk for chunk in chunks if chunk["key"] == key]
    if not file_chunks:
        raise SystemExit(f"no chunks for {key}")
    first = file_chunks[0]
    length = first["end"] - first["start"] + 1
    if first["kind"] in {"chapter", "front"} and length <= 20:
        return first
    return {
        "id": f"{key}-fallback20",
        "key": key,
        "file": first["file"],
        "kind": "fallback-slice",
        "title": "first 20 pages",
        "start": 1,
        "end": min(20, max(chunk["end"] for chunk in file_chunks)),
    }


def done_slices(chunk_id: str) -> set[str]:
    done = set()
    checkpoint = CHECKPOINT_DIR / "blocks.json"
    if checkpoint.exists():
        payload = json.loads(checkpoint.read_text(encoding="utf-8"))
        done.update(payload.get("done_slices", []))
    for record in iter_jsonl(BLOCKS_JSONL):
        if record.get("chunk") == chunk_id and record.get("slice"):
            done.add(record["slice"])
    return done


def mark_slice(slice_id: str) -> None:
    checkpoint = CHECKPOINT_DIR / "blocks.json"
    payload = {"done_slices": []}
    if checkpoint.exists():
        payload = json.loads(checkpoint.read_text(encoding="utf-8"))
    slices = set(payload.get("done_slices", []))
    slices.add(slice_id)
    write_json(checkpoint, {"done_slices": sorted(slices)})


def clear_chunk(chunk_id: str) -> None:
    kept = []
    for record in iter_jsonl(BLOCKS_JSONL):
        if record.get("_invalid") or record.get("chunk") == chunk_id:
            continue
        kept.append(record)
    if BLOCKS_JSONL.exists():
        rewrite_jsonl(BLOCKS_JSONL, kept)
    checkpoint = CHECKPOINT_DIR / "blocks.json"
    if checkpoint.exists():
        payload = json.loads(checkpoint.read_text(encoding="utf-8"))
        payload["done_slices"] = [item for item in payload.get("done_slices", []) if not item.startswith(chunk_id + ":")]
        write_json(checkpoint, payload)


def record_run(entry: dict) -> None:
    runs = []
    if BLOCKS_META.exists():
        payload = json.loads(BLOCKS_META.read_text(encoding="utf-8"))
        if isinstance(payload.get("runs"), list):
            runs = payload["runs"]
        elif payload.get("chunk_id"):
            runs = [payload]
    runs = [item for item in runs if item.get("chunk_id") != entry["chunk_id"]]
    runs.append(entry)
    write_json(BLOCKS_META, {"origin": entry["origin"], "model": entry.get("model"), "runs": runs})


def store_blocks(blocks: list[dict], chunk_id: str, slice_id: str, origin: str) -> None:
    for block in blocks:
        block["chunk"] = chunk_id
        block["slice"] = slice_id
        block["origin"] = origin
        if origin == "ollama":
            block["model"] = MODEL
        append_jsonl(BLOCKS_JSONL, block)
    mark_slice(slice_id)


def self_test() -> None:
    assert filter_topics(["nope", "01"], {"01", "unassigned"}) == ["01"]
    assert filter_topics(["nope"], {"01", "unassigned"}) == ["unassigned"]
    tax = {
        "topics": [
            {
                "id": "03/reaktionen/breakout",
                "level": "begriff",
                "begriff": "Breakout",
                "priority": "A",
                "haupt_id": "03",
            }
        ],
        "id_set": {"03/reaktionen/breakout", "unassigned"},
    }
    blocks = fallback_blocks_from_text(
        "A breakout above a prior high is valid only when volume expands by 150 percent of average. "
        "Traders wait for the close beyond the level before they act on that signal in the next session.",
        "x.pdf",
        3,
        tax,
    )
    assert blocks and blocks[0]["origin"] == "fallback_unreviewed"
    assert blocks[0]["topics"] == ["03/reaktionen/breakout"]
    source = "Traders wait for volume to expand by 150 percent of the average before they buy the breakout."
    assert grounded("Traders wait for volume to expand by 150 percent of the average before a buy.", source)
    assert not grounded("Traders wait for volume to expand by 999 percent of the average before a buy.", source)
    spray = {
        "topics": [
            {"id": "01/strukturwechsel/strukturbruch", "level": "begriff", "begriff": "Strukturbruch"},
            {"id": "01/strukturwechsel/trendfortsetzung", "level": "begriff", "begriff": "Trendfortsetzung"},
            {"id": "02/trendbestimmung/trenddauer", "level": "begriff", "begriff": "Trenddauer"},
            {"id": "01/preisbildung/marktstruktur", "level": "begriff", "begriff": "Marktstruktur"},
        ],
        "by_id": {},
    }
    spray["by_id"] = {topic["id"]: topic for topic in spray["topics"]}
    symmetry = (
        "When there is symmetry in market structure, which manifests itself in a traditional bell-shaped curve, "
        "there is generally a balance between good opportunities and bad."
    )
    sprayed = select_topics(
        symmetry,
        symmetry,
        ["01/strukturwechsel/strukturbruch", "01/strukturwechsel/trendfortsetzung", "01/preisbildung/marktstruktur"],
        spray,
        limit=1,
    )
    assert sprayed == ["01/preisbildung/marktstruktur"], sprayed
    credit = "The trend direction and duration are determined by the original theories pioneered by J. Peter Steidlmayer."
    assert select_topics(credit, credit, ["02/trendbestimmung/trenddauer"], spray) == ["unassigned"]
    print("extract_blocks self-test ok")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--list-chunks", action="store_true")
    parser.add_argument("--key", default="murphy")
    parser.add_argument("--chunk-id", default="")
    parser.add_argument("--redo", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return

    chunks = load_chunks()
    if args.chunk_id:
        selected = next(chunk for chunk in chunks if chunk["id"] == args.chunk_id)
    else:
        selected = select_body_chunk(chunks, args.key)
    if args.list_chunks:
        print_chunk_table(chunks, args.key, selected["id"])
        return

    tax = load_taxonomy()
    use_ollama = ollama_ready()
    if args.redo and use_ollama:
        clear_chunk(selected["id"])

    if not use_ollama:
        span = fallback_span(chunks, args.key)
        pages = load_pages(span["file"])
        written = 0
        for page in range(span["start"], span["end"] + 1):
            slice_id = f"{span['id']}:{page}"
            if slice_id in done_slices(span["id"]) and not args.redo:
                continue
            produced = fallback_blocks_from_text(pages.get(page, ""), span["file"], page, tax)
            for index, block in enumerate(produced, 1):
                block["id"] = f"b-{span['id']}-p{page}-{index:03d}"
            store_blocks(produced, span["id"], slice_id, "fallback_unreviewed")
            written += len(produced)
        record_run(
            {
                "origin": "fallback_unreviewed",
                "model": None,
                "chunk_id": span["id"],
                "file": span["file"],
                "start": span["start"],
                "end": span["end"],
                "blocks_written_this_run": written,
            }
        )
        print(f"fallback_unreviewed chunk={span['id']} pages={span['start']}-{span['end']} blocks={written}")
        return

    pages = load_pages(selected["file"])
    finished = done_slices(selected["id"])
    written = 0
    started = time.time()
    print(f"ollama model={MODEL} chunk={selected['id']} pages={selected['start']}-{selected['end']}", flush=True)
    ping, _reason = ollama_chat(
        [{"role": "user", "content": 'Return {"ok": true}'}],
        num_ctx=2048,
        num_predict=20,
    )
    print(f"model loaded in {time.time() - started:.1f}s response_chars={len(ping)}", flush=True)
    for start, end in slice_pairs(selected["start"], selected["end"], pages):
        slice_id = f"{selected['id']}:{start}-{end}"
        if slice_id in finished:
            print(f"skip {slice_id}", flush=True)
            continue
        total, _average = window_stats(pages, start, end)
        if total < 400:
            mark_slice(slice_id)
            print(f"skip thin {slice_id} chars={total}", flush=True)
            continue
        began = time.time()
        try:
            produced = ollama_slice(pages, selected, start, end, tax)
        except SystemExit:
            if start == end:
                mark_slice(slice_id)
                print(f"skip failed {slice_id}", flush=True)
                continue
            print(f"retry {slice_id} page by page", flush=True)
            produced = []
            for page in range(start, end + 1):
                try:
                    produced.extend(ollama_slice(pages, selected, page, page, tax))
                except SystemExit:
                    print(f"skip failed page {page}", flush=True)
        store_blocks(produced, selected["id"], slice_id, "ollama")
        written += len(produced)
        print(f"{slice_id} blocks={len(produced)} seconds={time.time() - began:.1f}", flush=True)
    record_run(
        {
            "origin": "ollama",
            "model": MODEL,
            "chunk_id": selected["id"],
            "file": selected["file"],
            "start": selected["start"],
            "end": selected["end"],
            "blocks_written_this_run": written,
        }
    )
    print(f"ollama chunk={selected['id']} new_blocks={written}")


if __name__ == "__main__":
    main()
