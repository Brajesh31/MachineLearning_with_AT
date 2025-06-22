# dictionary.py

# Creating a dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Accessing dictionary items
print(f"Name: {person['name']}")

# Modifying a dictionary
person["age"] = 31
print(f"Updated person: {person}")

# Adding new key-value pairs
person["email"] = "john@example.com"
print(f"After adding email: {person}")

# Removing items
person.pop("city")
print(f"After removing city: {person}")

# Iterating through a dictionary
for key, value in person.items():
    print(f"{key}: {value}")
