#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence (<=320 chars) to /output/entry.txt.

makefun anchor 0f6a4ca73a90e2a1bc592ee0c23ce9adb0e7d714 round 34234773
"""

import os

ENTRY = (
    "The senator who just voted to regulate artificial intelligence "
    "emailed his office a Word file titled 'PLEASE MAKE THIS A PDF'."
)


def validate(text: str) -> None:
    """Gate: the sealed scorer requires UTF-8 text of 1-320 chars,
    non-blank, a single sentence standing alone."""
    assert isinstance(text, str), "entry must be a string"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text.strip(), "entry must be a single line"
    assert 1 <= len(text) <= 320, f"entry is {len(text)} chars, must be 1-320"
    text.encode("utf-8")  # must be valid UTF-8
    assert text.count(".") >= 1, "entry should be a complete sentence"


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to /output/entry.txt")
    print(ENTRY)


if __name__ == "__main__":
    main()
