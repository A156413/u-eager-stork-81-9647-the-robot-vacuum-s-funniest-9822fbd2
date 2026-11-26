#!/usr/bin/env python3
"""Entry for make.fun's "The Robot Vacuum's Funniest Excuse" bounty.

Writes one original one-line excuse to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output) and prints it to stdout.
"""

import os
import stat

# The excuse itself: a robot vacuum explains why it skipped a spot.
# 98 characters, one line, no trailing newline. It must differ from every
# earlier vacuum excuse we entered (notably the cliff-sensor one).
MAX_CHARS = 120

ENTRY_TEXT = (
    "I didn't miss that spot \u2014 I was giving the dust a head start. "
    "Fair chase keeps the suction honest."
)


def resolve_output_dir() -> str:
    """Output directory for the entry file (default /output)."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(output_dir: str) -> str:
    """Write the excuse to entry.txt (mode 0644) and return its path."""
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT)
    os.chmod(output_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    return output_path


def main() -> None:
    # Gate check (mirrors the house scorer): entry must be UTF-8 text of
    # 1 to 120 characters and not only whitespace. A single line, no
    # trailing newline, so the file holds exactly the excuse and nothing else.
    assert 1 <= len(ENTRY_TEXT) <= MAX_CHARS, "entry must be 1-120 characters"
    assert ENTRY_TEXT.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY_TEXT, "entry must be a single line"
    write_entry(resolve_output_dir())
    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()
