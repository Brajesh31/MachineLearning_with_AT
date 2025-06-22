# vectors_matrix.py
import numpy as np

# Creating a vector
vector = np.array([1, 2, 3])

# Creating a matrix
matrix = np.array([[1, 2, 3], [4, 5, 6]])

print(f"Vector: {vector}")
print(f"Matrix: \n{matrix}")

# Transposing a matrix
transpose_matrix = matrix.T
print(f"Transposed Matrix: \n{transpose_matrix}")
