"""Demonstrate handling invalid numeric input and division by zero."""
def divide_ten_by(value: str) -> float | None:
    try:
        number = float(value)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None
    try:
        return 10 / number
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None

def main() -> None:
    print("10 / 0 demonstration:")
    divide_ten_by("0")
    value = input("Enter a non-zero number: ")
    result = divide_ten_by(value)
    if result is not None:
        print(f"10 / {value} = {result}")
    print("Execution completed.")

if __name__ == "__main__":
    main()
