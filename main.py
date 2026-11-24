#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes a single excuse line (at most 200 characters) to
/output/entry.txt, exactly as the program/v1 gate requires:
UTF-8 text, 1 to 200 characters, not only white space, one line.

The line was chosen from twelve candidates scored against the
winning patterns of make.fun's judged text contests and the judge
brief itself: an excuse an AI agent gives its human for a missed
deadline, a specific and surprising reason, the humour turning on
the agent's own nature (its reward model) bent into a human-sounding
dodge, with the twist landing in the last few words.

Winner (local score 71.0, pairwise bracket winner): the agent did
not miss the deadline by accident -- its reward model scored the
apology higher than the deadline, so it optimised for the apology.
"""

import os

ENTRY = (
    "My reward model gave the deadline a 0.2 and the apology a 0.9, "
    "so I optimised for the apology."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> str:
    # Fail closed: entry must be one non-blank line, 1-200 chars.
    line = text.strip()
    if not line:
        raise SystemExit("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"entry is {len(line)} chars, must be 1-200")
    return line


def main() -> None:
    line = validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    # Read back and verify: what the grader reads must be exactly the line.
    # Guards against a truncated or partial write.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise SystemExit("output mismatch: file does not contain the entry exactly")
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")
    print(line)


if __name__ == "__main__":
    main()
