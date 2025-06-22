# conditional_statements.py

# Example of if-else statements
age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Example of if-elif-else statements
marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")

# Example of nested if
number = 15

if number > 0:
    if number % 2 == 0:
        print(f"{number} is a positive even number.")
    else:
        print(f"{number} is a positive odd number.")
else:
    print(f"{number} is not positive.")
