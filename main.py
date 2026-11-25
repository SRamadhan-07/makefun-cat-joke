#!/usr/bin/env python3
"""Write the one-line cat joke entry to /output/entry.txt.

The joke: a cat's dead-mouse gift reframed as a performance bonus
in her own economy. Single line, 101 characters, within the
competition gate of 1 to 200 characters.
"""

import os

ENTRY_TEXT = "My cat brought me a dead mouse, which is generous, because in her economy that's a performance bonus."


def main() -> None:
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    # Write exactly the entry text, with no trailing newline, so the
    # file is a single line matching the approved joke byte for byte.
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
