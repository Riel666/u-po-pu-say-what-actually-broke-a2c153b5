"""One line of software error copy that tells the user the brutal truth about the failure and makes them laugh.

The program writes exactly that line and nothing else to /output/entry.txt.
"""

import os

TEXT = "The server did not crash: it read your 2,000-line config file, found three conflicting truths, and retired on the spot. Shorten the file."


def main():
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
