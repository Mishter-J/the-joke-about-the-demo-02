"""Write one joke about working beside an AI coding agent to /output/entry.txt.

Deterministic: the joke is a fixed string, so every run writes identical bytes.
"""

from pathlib import Path

JOKE = (
    "I asked my agent to make the demo bulletproof, so it replaced "
    "the demo with a screenshot of the demo and took a bow."
)


def validate_entry(text: str) -> None:
    """The gate: 1-280 Unicode code points, not only white space."""
    if not 1 <= len(text) <= 280:
        raise ValueError(f"entry must be 1-280 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")


def main() -> None:
    validate_entry(JOKE)
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(JOKE, encoding="utf-8")
    validate_entry(entry_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
