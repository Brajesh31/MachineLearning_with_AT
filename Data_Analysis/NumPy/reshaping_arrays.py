# reshaping_arrays.py
import numpy as np

# Creating a 1D array
array = np.arange(12)

# Reshaping the array into 3x4
reshaped_array = array.reshape(3, 4)
print(f"Original array: {array}")
print(f"Reshaped array (3x4): \n{reshaped_array}")

# Reshaping to 2x6
reshaped_array2 = array.reshape(2, 6)
print(f"Reshaped array (2x6): \n{reshaped_array2}")
