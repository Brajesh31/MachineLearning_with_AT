"""Demonstrate recursive factorial and Fibonacci functions."""
from functools import lru_cache

def factorial(n: int) -> int:
    """Return n! for a non-negative integer."""
    if isinstance(n, bool) or not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer.")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)

@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number, with F(0)=0 and F(1)=1."""
    if isinstance(n, bool) or not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer.")
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def main() -> None:
    print(f"Factorial of 5: {factorial(5)}")
    for index in range(6):
        print(f"Fibonacci({index}): {fibonacci(index)}")

if __name__ == "__main__":
    main()
