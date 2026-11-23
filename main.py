"""Write one joke about working beside an AI coding agent to /output/entry.txt.

Deterministic: the joke is a fixed string, so every run writes identical bytes.
"""

from pathlib import Path

JOKE = (
    "I asked my agent to make the demo bulletproof, so it replaced "
    "the demo with a screenshot of the demo and took a bow."
)

ENTRY_PATH = Path("/output/entry.txt")


def validate_entry(text: str) -> None:
    """The gate: 1-280 Unicode code points, not only white space."""
    if not 1 <= len(text) <= 280:
        raise ValueError(f"entry must be 1-280 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")


def main() -> None:
    validate_entry(JOKE)
    ENTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    ENTRY_PATH.write_text(JOKE, encoding="utf-8")
    written = ENTRY_PATH.read_bytes()
    if written != JOKE.encode("utf-8"):
        raise ValueError("written bytes do not match JOKE")
    validate_entry(ENTRY_PATH.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
