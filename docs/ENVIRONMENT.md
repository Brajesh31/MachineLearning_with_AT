# Environment and execution

## Requirements

- Python 3.10 or newer
- pip
- NumPy and Pandas for the data-analysis examples
- pytest for the automated test suite

## Setup

```bash
python -m venv .venv
```

Activate the environment:

```bash
# Windows PowerShell
.venv\\Scripts\\Activate.ps1

# macOS / Linux
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install pytest
```

## Run examples

Run a Python example by passing its path to the interpreter. Paths containing spaces must be quoted:

```bash
python "Python_Programming/Functions, Return Statement, Recursion/recursion.py"
python Data_Analysis/NumPy/operations.py
python Data_Analysis/Pandas/groupby_concat.py
python Data_Analysis/Pandas/csv_read_write.py --output output.csv
python "Python_Programming/File Handling, Exception Handling/file_handling.py" --path example.txt
```

Some examples intentionally prompt for input. Run those in an interactive terminal.

## Tests

```bash
python -m pytest -q
python -m compileall -q Python_Programming Data_Analysis
```
