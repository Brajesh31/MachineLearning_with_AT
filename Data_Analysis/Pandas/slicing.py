# slicing.py
import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['John', 'Jane', 'Jack'],
    'Age': [28, 24, 30],
    'Salary': [50000, 60000, 55000]
}
df = pd.DataFrame(data)

# Slicing rows by index
print("First two rows:")
print(df[:2])

# Slicing columns
print("\nName and Age columns:")
print(df[['Name', 'Age']])
