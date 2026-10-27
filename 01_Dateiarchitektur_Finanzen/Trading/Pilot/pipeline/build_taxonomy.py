"""Parse Themenstruktur.txt into a closed topic-id list.

IDs are haupt, gruppe, and begriff. The model may emit only these ids.
"""

from __future__ import annotations

import argparse
import re
import sys

from common import TAXONOMY_JSON, TAXONOMY_TXT, slug, write_json

HAUPT_RE = re.compile(r"^(\d+)\.\s+(.+?)\s*$")
BEGRIFF_RE = re.compile(r"^\[([ABC])\]\s+(.+?)\s*$")

SAMPLE = """
1. Alpha Thema

Erste Gruppe
[A] Begriff Eins
[B] Begriff Zwei

2. Beta

Zweite Gruppe
[C] Begriff Drei
[A] Begriff Eins
"""


def parse_taxonomy(text: str, source: str) -> dict:
    topics: list[dict] = []
    ids: list[str] = []
    seen: set[str] = set()
    haupt_id = haupt_name = gruppe_id = gruppe_name = None

    def add(topic: dict) -> None:
        topic_id = topic["id"]
        if topic_id in seen:
            raise SystemExit(f"duplicate topic id: {topic_id}")
        seen.add(topic_id)
        ids.append(topic_id)
        topics.append(topic)

    for line_no, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line:
            continue
        haupt_match = HAUPT_RE.match(line)
        if haupt_match:
            haupt_id = f"{int(haupt_match.group(1)):02d}"
            haupt_name = haupt_match.group(2).strip()
            gruppe_id = gruppe_name = None
            add(
                {
                    "id": haupt_id,
                    "level": "haupt",
                    "haupt_id": haupt_id,
                    "haupt": haupt_name,
                    "gruppe_id": None,
                    "gruppe": None,
                    "begriff": None,
                    "priority": None,
                }
            )
            continue
        begriff_match = BEGRIFF_RE.match(line)
        if begriff_match:
            if not haupt_id or not gruppe_id:
                raise SystemExit(f"begriff without haupt/gruppe at line {line_no}: {line}")
            priority, label = begriff_match.group(1), begriff_match.group(2).strip()
            base = slug(label)
            topic_id = f"{gruppe_id}/{base}"
            suffix = 2
            while topic_id in seen:
                topic_id = f"{gruppe_id}/{base}-{suffix}"
                suffix += 1
            add(
                {
                    "id": topic_id,
                    "level": "begriff",
                    "haupt_id": haupt_id,
                    "haupt": haupt_name,
                    "gruppe_id": gruppe_id,
                    "gruppe": gruppe_name,
                    "begriff": label,
                    "priority": priority,
                }
            )
            continue
        if not haupt_id:
            raise SystemExit(f"group before haupt at line {line_no}: {line}")
        gruppe_name = line
        base = slug(line)
        gruppe_id = f"{haupt_id}/{base}"
        suffix = 2
        while gruppe_id in seen:
            gruppe_id = f"{haupt_id}/{base}-{suffix}"
            suffix += 1
        add(
            {
                "id": gruppe_id,
                "level": "gruppe",
                "haupt_id": haupt_id,
                "haupt": haupt_name,
                "gruppe_id": gruppe_id,
                "gruppe": gruppe_name,
                "begriff": None,
                "priority": None,
            }
        )

    counts = {"haupt": 0, "gruppe": 0, "begriff": 0}
    priorities = {"A": 0, "B": 0, "C": 0}
    for topic in topics:
        counts[topic["level"]] += 1
        if topic["priority"]:
            priorities[topic["priority"]] += 1
    return {
        "source": source,
        "id_rule": "haupt / gruppe / begriff; unknown model ids become unassigned",
        "counts": counts,
        "priorities": priorities,
        "ids": ids,
        "topics": topics,
    }


def self_test() -> None:
    payload = parse_taxonomy(SAMPLE, "sample")
    assert payload["counts"] == {"haupt": 2, "gruppe": 2, "begriff": 4}, payload["counts"]
    assert "01/erste-gruppe/begriff-eins" in payload["ids"]
    assert "02/zweite-gruppe/begriff-eins" in payload["ids"]
    print("taxonomy self-test ok")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--source", type=str, default=str(TAXONOMY_TXT))
    parser.add_argument("--out", type=str, default=str(TAXONOMY_JSON))
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    source = TAXONOMY_TXT if args.source == str(TAXONOMY_TXT) else __import__("pathlib").Path(args.source)
    text = source.read_text(encoding="utf-8-sig")
    payload = parse_taxonomy(text, str(source))
    if payload["counts"]["haupt"] != 25:
        raise SystemExit(f"expected 25 haupt topics, got {payload['counts']['haupt']}")
    write_json(__import__("pathlib").Path(args.out), payload)
    print(
        f"wrote {args.out} haupt={payload['counts']['haupt']} "
        f"gruppe={payload['counts']['gruppe']} begriff={payload['counts']['begriff']} "
        f"A={payload['priorities']['A']} B={payload['priorities']['B']} C={payload['priorities']['C']}"
    )


if __name__ == "__main__":
    main()
