"""make.fun entry: One Line, No Deadline Met.

Writes one single-line joke excusing a missed deadline to
/output/entry.txt.

The excuse is a confession in disguise: the work was finished on
time, but reading it back was so bad that pretending never to have
started became the plan. The punch lands in the last few words,
and it sounds like something a cornered person would actually say.
"""

import os

ENTRY = (
    "I actually finished it on Tuesday, but when I read it back it "
    "was so bad I had to pretend I'd never started."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    tmp_path = "/output/.entry.txt.tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
