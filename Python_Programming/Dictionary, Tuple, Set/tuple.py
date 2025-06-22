# tuple.py

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements
print(f"First element: {my_tuple[0]}")

# Tuple is immutable, so we cannot change elements
# We can however iterate through the tuple
for item in my_tuple:
    print(f"Item: {item}")

# Tuple unpacking
a, b, c, d, e = my_tuple
print(f"Unpacked values: {a}, {b}, {c}, {d}, {e}")

# Finding length of tuple
print(f"Length of tuple: {len(my_tuple)}")
