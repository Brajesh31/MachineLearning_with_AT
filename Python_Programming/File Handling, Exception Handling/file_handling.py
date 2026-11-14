"""Write and read a UTF-8 text file using a caller-selected path."""
import argparse
from pathlib import Path

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", type=Path, default=Path("example.txt"))
    args = parser.parse_args()
    args.path.parent.mkdir(parents=True, exist_ok=True)
    args.path.write_text("This is a test file.\n", encoding="utf-8")
    content = args.path.read_text(encoding="utf-8")
    print(f"File content: {content.rstrip()}")
    print(f"File path: {args.path}")

if __name__ == "__main__":
    main()
