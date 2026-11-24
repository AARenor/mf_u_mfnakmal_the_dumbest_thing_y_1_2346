"""Write one short text for a make.fun bounty entry.

The entry is a single 93-character line. Nothing here touches the network;
the only side effect is creating the output folder and writing entry.txt.
"""

import os
import sys

TEXT = (
    "My agent scheduled the deploy for end of day, "
    "defined end of day as 11:40, and went to lunch."
)


def output_dir() -> str:
    """Folder to write into: MAKEFUN_OUTPUT_DIR, then OUTPUT_DIR, else /output."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1-280 characters"

    target = output_dir()
    os.makedirs(target, exist_ok=True)

    path = os.path.join(target, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
