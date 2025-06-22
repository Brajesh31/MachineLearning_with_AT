# strings.py

# Creating a string
my_string = "Hello, World!"

# Accessing characters
print(f"First character: {my_string[0]}")
print(f"Last character: {my_string[-1]}")

# String slicing
print(f"Substring: {my_string[0:5]}")  # Hello

# String methods
print(f"Uppercase: {my_string.upper()}")
print(f"Lowercase: {my_string.lower()}")
print(f"Replace 'World' with 'Python': {my_string.replace('World', 'Python')}")

# Splitting a string
words = my_string.split(", ")
print(f"Words: {words}")

# Joining a list into a string
joined_string = "-".join(words)
print(f"Joined string: {joined_string}")
