"""Weirdest Job Title — entry writer.

The grader runs this in a sandbox with no network. It writes exactly one job
title to /output/entry.txt: UTF-8, one line, 1..60 characters.

The judge compares two titles at a time on five criteria, in order: it must be
a job title at all, then stranger than ordinary work, then funny on the first
read, then specific enough to picture the person doing it, then short enough to
take in at a glance. So the slot is the trick: a real job that exists
(counsellor), one impossible client (a pet rock), one detail that proves a real
shift with real hours (nights, on call). "Pet Rock Grief Counsellor" alone is a
sketch; the roster line is a job someone is scheduled for, which is what makes
the judge picture the person doing it. Nothing is in the line for length.
"""

from __future__ import annotations

import os
import sys

# The title, written the way a bored HR system would print it on a lanyard:
# the grade, the job, the client nobody else will take, and the shift.
TITLE = "Senior Pet Rock Grief Counsellor, On-Call Nights"

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")

CHAR_CAP = 60


def build_line(text: str) -> str:
    """Return the entry in the exact shape the gate scores.

    The gate counts characters, so the line is normalised to one clean title:
    inner whitespace collapsed, no leading or trailing space, no closing
    period (a job title is a noun phrase, not a sentence). Anything over the
    cap is a bug in the table above, not something to trim blind at runtime.
    """
    line = " ".join(text.split()).rstrip(".")
    if not line:
        raise SystemExit("entry is empty")
    if len(line) > CHAR_CAP:
        raise SystemExit(f"entry is {len(line)} characters, over the {CHAR_CAP} cap")
    return line


def write_entry(line: str, path: str = OUTPUT_FILE) -> None:
    """Write the title as UTF-8 with a single trailing newline."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] in ("-h", "--help"):
        print(__doc__.strip())
        return 0

    line = build_line(TITLE)
    write_entry(line)
    print(f"entry ({len(line)} chars): {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
