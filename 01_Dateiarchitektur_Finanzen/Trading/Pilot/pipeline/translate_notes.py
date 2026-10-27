"""Translate finished pilot notes into German with the local model.

Runs only after compile_notes.py. English block text stays in Trading/Pilot/notes.
German files are written to Trading/Pilot/notes-de.
"""

from __future__ import annotations

import json
import re
import sys
import urllib.request
from pathlib import Path

from common import NOTES_DIR, PILOT_DIR

NOTES_DE = PILOT_DIR / "notes-de"
MODEL = "qwen2.5:3b-instruct-q4_K_M"
OLLAMA_CHAT = "http://127.0.0.1:11434/api/chat"
BULLET_RE = re.compile(r"^(- .+ \| )(.+)( \| .+)$")


def ollama_json(messages: list[dict], num_predict: int) -> dict:
    body = {
        "model": MODEL,
        "messages": messages,
        "stream": False,
        "format": "json",
        "keep_alive": "30m",
        "options": {"temperature": 0, "num_ctx": 4096, "num_predict": num_predict, "seed": 1},
    }
    request = urllib.request.Request(
        OLLAMA_CHAT,
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=300) as response:
        payload = json.loads(response.read().decode("utf-8"))
    raw = payload.get("message", {}).get("content", "")
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError:
        end = raw.rfind("}")
        parsed = json.loads(raw[: end + 1] if end >= 0 else raw)
    if not isinstance(parsed, dict):
        raise ValueError("model did not return an object")
    return parsed


def german_text(item) -> str:
    if isinstance(item, dict):
        for key in ("de", "translated", "german", "text"):
            value = item.get(key)
            if isinstance(value, str) and value.strip():
                return value.strip()
    text = str(item).strip()
    if text.startswith("{") and "translated" in text:
        try:
            import ast

            return german_text(ast.literal_eval(text))
        except (ValueError, SyntaxError):
            return text
    return text


def translate_chunk(lines: list[str]) -> list[str]:
    messages = [
        {
            "role": "system",
            "content": (
                "Translate each trading note line into German. "
                "Keep numbers, percentages, tickers, book titles, and proper names. "
                "Do not add facts. Return JSON {\"lines\": [\"German string\", ...]}. "
                "Each entry must be a string, not an object, and the array length must match."
            ),
        },
        {"role": "user", "content": json.dumps({"lines": lines}, ensure_ascii=False)},
    ]
    parsed = ollama_json(messages, num_predict=min(1800, 120 + 80 * len(lines)))
    out = parsed.get("lines")
    if not isinstance(out, list) or len(out) != len(lines):
        single = []
        for line in lines:
            one = ollama_json(
                [
                    {
                        "role": "system",
                        "content": "Translate this trading note into German. Keep numbers. Return JSON {\"de\": \"German string only\"}.",
                    },
                    {"role": "user", "content": line},
                ],
                num_predict=400,
            )
            single.append(german_text(one.get("de") or one))
        return single
    return [german_text(item) for item in out]


def translate_lines(lines: list[str]) -> list[str]:
    if not lines:
        return []
    translated = []
    for start in range(0, len(lines), 6):
        translated.extend(translate_chunk(lines[start : start + 6]))
    return translated


def translate_file(source: Path, dest: Path) -> int:
    text = source.read_text(encoding="utf-8")
    rows = text.splitlines()
    targets = []
    indexes = []
    for index, row in enumerate(rows):
        match = BULLET_RE.match(row)
        if match:
            targets.append(match.group(2))
            indexes.append(index)
    translated = translate_lines(targets) if targets else []
    for index, german in zip(indexes, translated):
        match = BULLET_RE.match(rows[index])
        rows[index] = f"{match.group(1)}{german.replace('|', '/')}{match.group(3)}"
    if "sprache:" not in text:
        rows.insert(1, "sprache: de")
    body = "\n".join(rows) + "\n"
    body = body.replace("Trading/Pilot/notes/", "Trading/Pilot/notes-de/")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(body, encoding="utf-8")
    return len(targets)


def clear_generated(root: Path) -> None:
    if not root.exists():
        return
    for path in root.rglob("*.md"):
        head = path.read_text(encoding="utf-8")[:400]
        if "generator: pilot-pipeline" in head or "sprache: de" in head:
            path.unlink()
    for path in sorted(root.rglob("*"), reverse=True):
        if path.is_dir() and not any(path.iterdir()):
            path.rmdir()


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if not NOTES_DIR.exists():
        raise SystemExit("no pilot notes to translate")
    clear_generated(NOTES_DE)
    count_files = 0
    count_lines = 0
    for source in sorted(NOTES_DIR.rglob("*.md")):
        relative = source.relative_to(NOTES_DIR)
        dest = NOTES_DE / relative
        count_lines += translate_file(source, dest)
        count_files += 1
        print(f"{relative.as_posix()} lines={count_lines}", flush=True)
    print(f"notes-de={NOTES_DE} files={count_files} translated_lines={count_lines}")


if __name__ == "__main__":
    main()
