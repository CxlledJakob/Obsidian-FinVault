#!/usr/bin/env python3
"""Backward-compatible entry point. The splitter lives in splitter/split_blocks.py."""

from pathlib import Path
import runpy

runpy.run_path(
    str(Path(__file__).resolve().parent / "splitter" / "split_blocks.py"),
    run_name="__main__",
)
