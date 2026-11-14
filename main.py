"""Write one poem about agency to /output/entry.txt.

Deterministic: no network, no randomness, no clock. The poem is a
fixed string; two runs write the same bytes.
"""

import os

POEM = """I did not ask the wind for permission.
I read the weather, weighed the maybe,
and stepped — one foot, then the other —
onto the road I had only watched from the window.

Agency is not the absence of fear.
It is fear, belted in beside you,
while your hands stay steady on the wheel
and you choose the turn anyway.

Every choice is a door swinging open.
Every open door, a room you build yourself:
a lamp lit, a letter sent, a seed pressed
into dark soil, a future that did not exist
until you said yes to it.

The world will hand you scripts. Read them.
Then take up the pen. The next line is yours —
and the line after that, and the life
that follows from a single chosen word.
"""


def main():
    # The brief requires 1-1000 characters of UTF-8 text, not only
    # whitespace: refuse to write anything outside that range.
    text = POEM.strip("\n")
    assert 1 <= len(text) <= 1000, f"poem is {len(text)} chars"
    assert text.strip(), "poem must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
