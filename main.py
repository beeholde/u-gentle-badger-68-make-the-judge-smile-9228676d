#!/usr/bin/env python3
"""Make the Judge Smile — entry program.

Writes one line (at most 200 characters) about a small good thing that
happened today to /output/entry.txt, with no trailing newline.

The line: a baker sang happy birthday to a stranger whose birthday it
isn't; the stranger blew out the candle on someone else's cake and
wished for them instead. Warmth first (a selfless wish), then the
surprise (it isn't my birthday), then one concrete detail (the candle
on someone else's cake), in fresh wording.
"""

import os
from pathlib import Path

MAX_CHARS = 200  # gate: entry.txt must be 1-200 characters

LINE = (
    "It isn't my birthday, but the baker sang anyway \u2014 "
    "I blew out the candle on someone else's cake "
    "and wished for them instead."
)


def main() -> None:
    text = LINE.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(f"line is {len(text)} chars, must be 1-{MAX_CHARS}")
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
