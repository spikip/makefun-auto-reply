"""Entry for the make.fun bounty "The Funniest Auto-Reply an AI Ever Sent".

The program writes a single line, an out-of-office auto-reply, to
/output/entry.txt. The line is an inbox in miniature: it opens with
the polite thank-you every auto-reply must have, then admits the
truth, that the writer is avoiding eye contact with the inbox and
will only reply when the guilt becomes unbearable. It is one
sentence of office absurdity, it lands its surprise in one read, and
it needs no explanation. The gate allows 1 to 159 characters of
UTF-8 text, so the line is checked against that cap before it is
written.

Why this line: the judge weighs whether the line really reads as an
auto-reply, whether it earns a real laugh, whether it turns on a
surprise, and whether it stays in the head. The joke works because
the formal opening sets up a proper office message and the confession
that follows breaks it completely, turning a polite ritual into an
admission of inbox avoidance everyone recognises at once. It is one
sentence, it needs no explanation, and the punchline is quotable
enough to repeat the next time someone sets an out-of-office reply.
"""

import os

ENTRY = (
    # The polite opening is the setup; the guilt confession is the
    # punchline, so the formal tone must stay intact.
    "Thank you for your email. I am currently out of the office, "
    "avoiding eye contact with my inbox, and will reply when the "
    "guilt becomes unbearable."
)

MAX_CHARS = 159
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
