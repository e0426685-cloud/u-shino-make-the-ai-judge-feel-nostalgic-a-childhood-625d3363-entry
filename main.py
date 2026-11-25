"""Write one childhood-memory sentence to /output/entry.txt.

Entry for make.fun bounty u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363:
"Make the AI Judge Feel Nostalgic: A Childhood Memory".

Stdlib only. Deterministic: the sentence is a fixed string.
"""

import os
import stat

ENTRY = (
    "On summer evenings my grandmother lifted the lid off the rice cooker "
    "with a wooden spoon, and the steam fogged her glasses while I stood on "
    "a stool behind her, stealing the crisp golden rice from the bottom of "
    "the pot before she could scrape it into my bowl."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Check the entry meets the gate: one sentence, 1-280 chars, non-blank."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) > 280:
        raise ValueError("entry is %d chars, over the 280 limit" % len(text))
    if len(text) < 1:
        raise ValueError("entry is empty")
    # One sentence: exactly one sentence-ending mark, at the very end.
    endings = sum(text.count(c) for c in ".!?")
    if endings != 1:
        raise ValueError("entry must be exactly one sentence")
    if text[-1] not in ".!?":
        raise ValueError("entry must end with its sentence-ending mark")
    return True


def main():
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    print("wrote %d chars to %s" % (len(ENTRY), OUTPUT_PATH))


if __name__ == "__main__":
    main()
