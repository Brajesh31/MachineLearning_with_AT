# diagonal_trace.py
import numpy as np

# Creating a square matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Extracting diagonal
diagonal = np.diag(matrix)
print(f"Diagonal of the matrix: {diagonal}")

# Computing trace (sum of diagonal elements)
trace = np.trace(matrix)
print(f"Trace of the matrix: {trace}")
