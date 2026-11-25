#!/usr/bin/env python3
"""One Star, Written in Sap — one-line 1-star houseplant review.

Writes a single-line review to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Stdlib only.
"""

import os

ENTRY = (
    "One star. He waters me with ice cubes, moves me six times a week "
    "'for the light', and calls me low-maintenance. I'm not a plant, "
    "I'm a hostage with leaves."
)


def main() -> None:
    if not (1 <= len(ENTRY) <= 279):
        raise SystemExit("entry length %d outside gate 1-279" % len(ENTRY))
    if not ENTRY.strip():
        raise SystemExit("entry is whitespace only")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    # Read-back guard: confirm what landed on disk is exactly the entry.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        raise SystemExit("read-back mismatch: entry on disk differs")
    if not (1 <= len(written) <= 279):
        raise SystemExit("written entry length %d outside gate 1-279" % len(written))


if __name__ == "__main__":
    main()
