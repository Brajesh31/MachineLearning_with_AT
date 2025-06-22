# recursion.py

# Recursive function to calculate factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Calling the recursive function
print(f"Factorial of 5: {factorial(5)}")

# Recursive function to calculate Fibonacci series
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Calling the Fibonacci function
for i in range(6):
    print(f"Fibonacci({i}): {fibonacci(i)}")
