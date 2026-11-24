"""Write one funny single-line developer excuse to entry.txt.

Deterministic: the same line is written on every run. The line is
104 characters, a single line with no trailing newline, inside the
competition gate of 1-200 characters of UTF-8 text.
"""

import os

EXCUSE = (
    "The cleanup cron I wrote to delete old sessions has been "
    "diligently deleting the new ones since Tuesday."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
