# series_dataframes.py
import pandas as pd

# Creating a Series
series = pd.Series([10, 20, 30, 40])
print("Series:")
print(series)

# Creating a DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)

# Accessing a column as a Series
print("\nColumn A as Series:")
print(df['A'])
