"""The Printer Apology: a make.fun bounty entry.

Writes one line, an apology note from an office printer to the people
who keep jamming it, feeding it cheap paper and swearing at it, to
/output/entry.txt. The entry is at most 120 characters, as the bounty
requires. The program is fully deterministic: same input, same output,
every run, with no randomness, no network and no time dependence.
"""

import os
import sys

ENTRY = (
    "Sorry I jammed. You feed me paper thinner than your patience, "
    "swear at me, and I am the one who has to say sorry."
)

OUTPUT_PATH = "/output/entry.txt"


def write_entry(path, text):
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main() -> None:
    assert 1 <= len(ENTRY) <= 120, "entry must be 1 to 120 characters"
    assert ENTRY.strip() != "", "entry must not be only whitespace"
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = os.environ.get("OUTPUT_PATH", OUTPUT_PATH)
    write_entry(path, ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
