# Python, Data Analysis, and Machine Learning Learning Repository

A practical collection of beginner-friendly Python examples and introductory notes covering programming fundamentals, data structures, control flow, functions, object-oriented programming, NumPy, Pandas, neural networks, and Generative AI.

The repository is organized by topic so individual examples can be read and executed independently.

## Contents

- [Learning path](#learning-path)
- [Repository structure](#repository-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Run examples](#run-examples)
- [Data analysis examples](#data-analysis-examples)
- [Generative AI and neural networks](#generative-ai-and-neural-networks)
- [Testing](#testing)
- [Contributing](#contributing)
- [Limitations](#limitations)
- [License](#license)

## Learning path

| Stage | Topic | What you learn |
| --- | --- | --- |
| 1 | Python basics | Variables, types, operators, conditions |
| 2 | Collections | Lists, strings, dictionaries, tuples, sets |
| 3 | Control flow | For/while loops, nested loops, break, continue, loop else |
| 4 | Functions | Parameters, return values, recursion |
| 5 | OOP | Classes, encapsulation, inheritance, polymorphism |
| 6 | File and exception handling | Text files, errors, input validation |
| 7 | NumPy | Arrays, vector/matrix operations, reshaping, statistics |
| 8 | Pandas | Series, DataFrames, CSV, missing values, grouping |
| 9 | AI foundations | Neural-network and Generative AI notes |

For a detailed topic-by-topic sequence, see [docs/LEARNING_PATH.md](docs/LEARNING_PATH.md).

## Repository structure

```text
.
├── Python_Programming/
│   ├── Python basics, Variables, Operators, Conditional Statements/
│   ├── Lists and Strings/
│   ├── Dictionary, Tuple, Set/
│   ├── For Loop, Break, and Continue statements/
│   ├── Loops/
│   ├── Functions, Return Statement, Recursion/
│   ├── Object-Oriented Programming (OOP)/
│   └── File Handling, Exception Handling/
├── Data_Analysis/
│   ├── NumPy/
│   └── Pandas/
├── Neural_Network/
├── GenerativeAI/
├── tests/
├── docs/
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10 or newer
- pip
- NumPy and Pandas
- pytest for running automated tests

## Installation

Clone the repository:

```bash
git clone https://github.com/Brajesh31/MachineLearning_with_AT.git
cd MachineLearning_with_AT
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

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

Run a script directly with Python. Quote paths containing spaces:

```bash
python "Python_Programming/Python basics, Variables, Operators, Conditional Statements/variables.py"
python "Python_Programming/Functions, Return Statement, Recursion/recursion.py"
python "Python_Programming/Object-Oriented Programming (OOP)/inheritance.py"
python Data_Analysis/NumPy/operations.py
python Data_Analysis/Pandas/groupby_concat.py
```

Some examples prompt for user input. Run those in an interactive terminal.

### File handling

The text-file example accepts a destination path:

```bash
python "Python_Programming/File Handling, Exception Handling/file_handling.py" --path output/example.txt
```

### CSV input and output

The CSV example uses an in-memory demonstration DataFrame if no input is provided:

```bash
python Data_Analysis/Pandas/csv_read_write.py --output output/example.csv
```

To read an existing CSV:

```bash
python Data_Analysis/Pandas/csv_read_write.py --input data.csv --output output/cleaned.csv
```

## Data analysis examples

### NumPy

The `Data_Analysis/NumPy/` folder demonstrates:

- Creating vectors and matrices.
- Transposing arrays.
- Element-wise arithmetic, dot products, and cross products.
- Reshaping arrays without changing element count.
- Extracting matrix diagonals and calculating traces.
- Calculating mean, variance, and standard deviation.

### Pandas

The `Data_Analysis/Pandas/` folder demonstrates:

- Creating Series and DataFrames.
- Reading and writing CSV files.
- Selecting rows and columns.
- Detecting, filling, and dropping missing values.
- Grouping records and concatenating DataFrames.

The examples use small synthetic datasets. Do not use demonstration values as real business or financial data.

## Generative AI and neural networks

- [Generative AI fundamentals notes](GenerativeAI/Fundamentals_notes.md) cover tokens, prompt injection, fine-tuning, governance, and production concepts.
- [Neural network overview](Neural_Network/neural_network.md) introduces layers, neurons, and learning.

These are study notes, not authoritative or continuously updated references. Vendor capabilities, model availability, model licenses, and legal requirements change. Verify current claims against primary documentation before using them in a project.

## Testing

Run the automated tests:

```bash
python -m pytest -q
```

Compile the learning examples:

```bash
python -m compileall -q Python_Programming Data_Analysis
```

GitHub Actions tests the repository on Python 3.10 and 3.12, runs the NumPy and Pandas examples, scans Python code with CodeQL, and checks Markdown formatting.

## Contributing

Contributions that improve correctness, readability, accessibility for beginners, or test coverage are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting changes.

## Limitations

This is an educational code collection, not a production-ready Python package or a complete machine-learning curriculum. Some examples are intentionally small and use fixed demonstration data. Interactive scripts require terminal input. See [docs/KNOWN_LIMITATIONS.md](docs/KNOWN_LIMITATIONS.md).

## License

Original project material that the maintainer owns or is authorized to license is provided under the MIT License. See [LICENSE](LICENSE). Third-party dependencies and materials retain their respective licenses.

## Maintainer

Brajesh Kumar

Last updated: 2026-11-14 05:20 UTC
