"""Read a CSV file or create a small example, then write a normalized output."""
import argparse
from pathlib import Path
import pandas as pd

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, help="Optional input CSV. If omitted, use an in-memory example.")
    parser.add_argument("--output", type=Path, default=Path("output.csv"))
    args = parser.parse_args()

    if args.input:
        if not args.input.is_file():
            parser.error(f"Input CSV does not exist: {args.input}")
        frame = pd.read_csv(args.input)
    else:
        frame = pd.DataFrame({"Name": ["Asha", "Ravi"], "Score": [92, 87]})

    args.output.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(args.output, index=False)
    print("Data:")
    print(frame)
    print(f"\nWrote {len(frame)} rows to {args.output}")

if __name__ == "__main__":
    main()
