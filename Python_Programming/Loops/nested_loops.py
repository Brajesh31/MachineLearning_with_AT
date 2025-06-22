# nested_loops.py

# Example of nested for loops
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i: {i}, j: {j}")

# Nested while loops
x = 1
while x <= 3:
    y = 1
    while y <= 3:
        print(f"x: {x}, y: {y}")
        y += 1
    x += 1
