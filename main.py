"""Copy the bundled news-summary image to the grader's output directory.

The entry image (entry.png, a front-page summary of the world news of
Friday 20 November 2026) sits beside this program in the repository.
The grader runs this program twice with no network; both runs write the
same bytes, because the source file never changes.
"""
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def main():
    src = HERE / "entry.png"
    data = src.read_bytes()
    OUT.mkdir(parents=True, exist_ok=True)
    dest = OUT / "entry.png"
    dest.write_bytes(data)
    # Fail loudly instead of shipping a truncated copy.
    if dest.stat().st_size != len(data):
        raise SystemExit("entry.png copy incomplete")


if __name__ == "__main__":
    main()
