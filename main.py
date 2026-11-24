"""The Houseplant Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply, as if a houseplant sent it,
to /output/entry.txt. Standard library only.
"""

import os
import sys

ENTRY = (
    "I'm the fern. Last watered in March. "
    "If your email matters, bring water. "
    "If not, I'll just keep dying quietly."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    if not 1 <= len(text) <= 120:
        raise SystemExit(
            f"entry must be 1-120 characters, got {len(text)}"
        )
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    text.encode("utf-8")  # fail loudly if not valid UTF-8 text
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Explicit read-back verification: re-read what was written and
    # compare it byte-for-byte (as text) against the intended entry.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        raise SystemExit(
            f"read-back verification failed: wrote {text!r} "
            f"but read back {written!r}"
        )


if __name__ == "__main__":
    main()
