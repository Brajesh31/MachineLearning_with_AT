from pathlib import Path
import importlib.util
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

def load_module(relative_path: str, name: str):
    path = ROOT / relative_path
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module

def test_factorial_and_fibonacci_boundaries():
    module = load_module(
        "Python_Programming/Functions, Return Statement, Recursion/recursion.py",
        "recursion_examples",
    )
    assert module.factorial(0) == 1
    assert module.factorial(5) == 120
    assert [module.fibonacci(i) for i in range(7)] == [0, 1, 1, 2, 3, 5, 8]

def test_recursive_functions_reject_invalid_values():
    module = load_module(
        "Python_Programming/Functions, Return Statement, Recursion/recursion.py",
        "recursion_examples_invalid",
    )
    for function in (module.factorial, module.fibonacci):
        for value in (-1, 1.5, True):
            try:
                function(value)
            except ValueError:
                pass
            else:
                raise AssertionError(f"{function.__name__} accepted {value!r}")

def test_groupby_example_runs_without_mixed_type_aggregation():
    script = ROOT / "Data_Analysis/Pandas/groupby_concat.py"
    result = subprocess.run([sys.executable, str(script)], check=True, capture_output=True, text=True)
    assert "Average salary by department" in result.stdout
    assert "Concatenated DataFrame" in result.stdout

def test_csv_example_creates_output_without_external_input(tmp_path: Path):
    script = ROOT / "Data_Analysis/Pandas/csv_read_write.py"
    output = tmp_path / "nested" / "result.csv"
    subprocess.run(
        [sys.executable, str(script), "--output", str(output)],
        check=True, capture_output=True, text=True,
    )
    assert output.is_file()
    assert "Name,Score" in output.read_text(encoding="utf-8")

def test_file_handling_example_uses_requested_path(tmp_path: Path):
    script = ROOT / "Python_Programming/File Handling, Exception Handling/file_handling.py"
    target = tmp_path / "nested" / "example.txt"
    subprocess.run(
        [sys.executable, str(script), "--path", str(target)],
        check=True, capture_output=True, text=True,
    )
    assert target.read_text(encoding="utf-8") == "This is a test file.\n"

def test_all_python_examples_compile():
    import compileall
    assert compileall.compile_dir(str(ROOT / "Python_Programming"), quiet=1)
    assert compileall.compile_dir(str(ROOT / "Data_Analysis"), quiet=1)
