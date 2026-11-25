"""Museum of the Year 3000 — make.fun bounty entry.

Writes a single museum label, as a museum in the year 3000 would place it
beside an ordinary object from today, to /output/entry.txt.

The label is fixed and deterministic: the grader runs the program twice and
both runs must produce the same text. No network, no clock, no randomness.
"""

from __future__ import annotations

import os
from pathlib import Path

# The label: a CAPTCHA "I am not a robot" checkbox, misread by a year-3000
# curator as a solemn daily ritual for proving one's humanity — a ritual the
# robots performed too. Short, deadpan, and the joke lands in the last line.
LABEL = (
    "Checkbox, 'I Am Not a Robot', c. 2025. "
    "Visitors clicked it daily to prove they were human. "
    "The robots clicked it too."
)

MAX_CHARS = 200


def validate(text: str) -> str:
    """Gate check, mirroring the sealed scorer: 1-200 chars, not blank."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry is blank")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main() -> None:
    text = validate(LABEL)
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text + "\n", encoding="utf-8")
    print(f"wrote {len(text)} chars to {output_path}")


if __name__ == "__main__":
    main()