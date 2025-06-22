# set.py

# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding an element
my_set.add(6)
print(f"Set after adding 6: {my_set}")

# Removing an element
my_set.remove(2)
print(f"Set after removing 2: {my_set}")

# Checking membership
print(f"Is 3 in the set?: {3 in my_set}")

# Set operations (Union, Intersection)
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union = set1 | set2
intersection = set1 & set2

print(f"Union: {union}")
print(f"Intersection: {intersection}")
