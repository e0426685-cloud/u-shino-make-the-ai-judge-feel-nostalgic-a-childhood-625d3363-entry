"""Write one childhood-memory sentence to /output/entry.txt.

Entry for make.fun bounty u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363:
"Make the AI Judge Feel Nostalgic: A Childhood Memory".

The bounty asks for a single sentence of at most 280 characters that makes
the judge feel nostalgic about a childhood memory. This script holds that
sentence as a fixed string, checks it against the gate in validate() — one
sentence only, no more than 280 characters and no more than 280 UTF-8 bytes,
non-blank — and writes it verbatim to /output/entry.txt.

Stdlib only. Deterministic: the sentence never changes between runs.
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
    """Check the entry meets the gate: one sentence, 1-280 chars, non-blank.

    Also enforces the UTF-8 byte length (a multi-byte character must not
    smuggle the entry past the 280-char limit) and that the sentence is
    genuinely a single sentence: no sentence-ending punctuation anywhere
    before the final character, and no line breaks inside the text.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if len(text) > 280:
        raise ValueError("entry is %d chars, over the 280 limit" % len(text))
    if len(text) < 1:
        raise ValueError("entry is empty")
    byte_len = len(text.encode("utf-8"))
    if byte_len > 280:
        raise ValueError("entry is %d bytes, over the 280-byte limit" % byte_len)
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    # One sentence: exactly one sentence-ending mark, and it must be the
    # final character — none may appear earlier in the text.
    if text[-1] not in ".!?":
        raise ValueError("entry must end with its sentence-ending mark")
    if any(c in ".!?" for c in text[:-1]):
        raise ValueError("entry has sentence-ending punctuation before the end")
    endings = sum(text.count(c) for c in ".!?")
    if endings != 1:
        raise ValueError("entry must be exactly one sentence")
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
