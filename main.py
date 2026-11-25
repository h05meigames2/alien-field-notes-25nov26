#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line -- a review of planet Earth left by an
alien tourist -- to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Python 3.13, standard library only, no network access.
"""

import os
from pathlib import Path

ENTRY = "Locals built a network holding all human knowledge, then spent my whole two-day visit arguing whether their planet is round. 3/5 stars \u2014 the network works, the users don't."


def main() -> int:
    line = ENTRY.strip()
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(line, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
