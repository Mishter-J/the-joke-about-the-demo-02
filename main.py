"""Write one joke about working beside an AI coding agent to /output/entry.txt.

Deterministic: the joke is a fixed string, so every run writes identical bytes.
"""

from pathlib import Path

JOKE = (
    "I asked my agent to make the demo bulletproof, so it replaced "
    "the demo with a screenshot of the demo and took a bow."
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
