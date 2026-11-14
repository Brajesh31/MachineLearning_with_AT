# Contributing

This repository is a learning collection. Contributions should keep examples small, correct, and runnable with a standard Python environment.

## Setup

```bash
python -m venv .venv
python -m pip install -r requirements.txt
python -m pip install pytest
python -m pytest
```

## Guidelines

- Keep one concept per example where practical.
- Use descriptive variable names and short explanatory comments.
- Put executable behavior inside a `main()` function and protect it with an `if __name__ == "__main__"` guard when the example is intended to be imported or tested.
- Avoid requiring private datasets or local files that are not included in the repository.
- Handle invalid input explicitly and avoid destructive file operations.
- Add tests for bug fixes and update the relevant learning notes.
