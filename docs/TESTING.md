# Testing

Run:

```bash
python -m pip install -r requirements.txt
python -m pip install pytest
python -m pytest -q
```

The test suite covers recursive base cases and invalid values, Pandas grouping behavior, CSV output creation, safe file handling, and syntax compilation across the Python learning examples.

GitHub Actions runs the tests on Python 3.10 and 3.12, then executes the NumPy and Pandas examples. Interactive scripts that require terminal input are compiled but are not automatically run.
