# mean_variance_std.py
import numpy as np

# Creating a 2D array
data = np.array([[10, 20, 30], [40, 50, 60]])

# Calculating mean
mean = np.mean(data)
print(f"Mean: {mean}")

# Calculating variance
variance = np.var(data)
print(f"Variance: {variance}")

# Calculating standard deviation
std_dev = np.std(data)
print(f"Standard Deviation: {std_dev}")
