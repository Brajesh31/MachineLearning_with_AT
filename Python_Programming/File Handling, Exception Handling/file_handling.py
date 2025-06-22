# file_handling.py

# Writing to a file
with open("example.txt", "w") as file:
    file.write("This is a test file.")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(f"File content: {content}")
