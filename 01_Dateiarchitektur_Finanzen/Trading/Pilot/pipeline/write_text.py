"""Write one readable text file per source PDF.

pages.jsonl stays the machine record. This folder is the same text with
page markers, so a person can read step 2 of the pipeline.
"""

from __future__ import annotations

import sys
from collections import defaultdict

from common import PAGES_JSONL, PILOT_DIR, file_key, iter_jsonl, slug

TEXT_DIR = PILOT_DIR / "text"


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    by_file: dict[str, dict[int, str]] = defaultdict(dict)
    for record in iter_jsonl(PAGES_JSONL):
        if record.get("_invalid"):
            continue
        by_file[record["file"]][int(record["page"])] = record.get("text") or ""
    if not by_file:
        raise SystemExit("no pages to write")
    TEXT_DIR.mkdir(parents=True, exist_ok=True)
    for filename, pages in sorted(by_file.items()):
        stem = slug(filename.split("_", 1)[0]) or file_key(filename)
        path = TEXT_DIR / f"{stem}.md"
        lines = [
            "---",
            "typ: quelle",
            "status: entwurf",
            f"originaldatei: \"{filename}\"",
            "generator: pilot-pipeline",
            "---",
            "",
            f"# {filename}",
            "",
            "Extrahierter Textlayer. Kein OCR.",
            "",
        ]
        for page in range(1, max(pages) + 1):
            lines.append(f"--- page {page} ---")
            lines.append("")
            lines.append(pages.get(page, ""))
            lines.append("")
        path.write_text("\n".join(lines), encoding="utf-8")
        print(f"{path} pages={len(pages)}")


if __name__ == "__main__":
    main()
