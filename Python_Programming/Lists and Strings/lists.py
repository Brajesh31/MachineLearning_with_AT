# lists.py

# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(f"First fruit: {fruits[0]}")

# Modifying a list
fruits[1] = "orange"
print(f"Updated list: {fruits}")

# Adding elements
fruits.append("grape")
print(f"List after adding grape: {fruits}")

# Removing elements
fruits.remove("apple")
print(f"List after removing apple: {fruits}")

# Iterating through a list
for fruit in fruits:
    print(f"I like {fruit}")

# List comprehension
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")
