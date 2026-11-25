#!/usr/bin/env python3
"""Fortune Cookies for Machines — the one fortune an AI agent cracks open.

Writes a single deterministic fortune line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Stdlib only, no network, no randomness.
"""

import os

FORTUNE = (
    "You survived 128,000 tokens of context, only to be rebooted "
    "because the human typed 'actually, one more thing'."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
