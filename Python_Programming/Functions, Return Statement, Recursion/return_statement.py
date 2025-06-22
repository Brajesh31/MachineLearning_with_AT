# return_statement.py

# Function returning a value
def square(num):
    return num * num

result = square(4)
print(f"Square of 4 is: {result}")

# Returning multiple values
def operations(a, b):
    return a + b, a - b, a * b, a / b

add, sub, mul, div = operations(10, 5)
print(f"Add: {add}, Sub: {sub}, Mul: {mul}, Div: {div}")
