#!/usr/bin/env python3
"""Turn every PDF in a folder into one Markdown file with page markers.

    python3 parse_pdf.py --pdf-dir /pfad/zu/den/pdfs
    python3 parse_pdf.py --self-test

The Markdown files land in Trading/Pilot/text. The splitter reads them next.
"""

from __future__ import annotations

import sys

import extract_text
import write_text


def main() -> None:
    extract_text.main()
    if "--self-test" in sys.argv:
        return
    write_text.main()


if __name__ == "__main__":
    main()
