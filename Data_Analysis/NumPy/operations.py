# operations.py
import numpy as np

# Vectors for operations
vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

# Addition
addition = vector_a + vector_b
print(f"Addition: {addition}")

# Subtraction
subtraction = vector_a - vector_b
print(f"Subtraction: {subtraction}")

# Element-wise multiplication
multiplication = vector_a * vector_b
print(f"Multiplication: {multiplication}")

# Dot product
dot_product = np.dot(vector_a, vector_b)
print(f"Dot product: {dot_product}")

# Cross product
cross_product = np.cross(vector_a, vector_b)
print(f"Cross product: {cross_product}")
