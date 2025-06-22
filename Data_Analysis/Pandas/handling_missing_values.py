# handling_missing_values.py
import pandas as pd
import numpy as np

# Creating a DataFrame with missing values
data = {
    'Name': ['John', 'Jane', np.nan],
    'Age': [28, np.nan, 30],
    'Salary': [50000, 60000, np.nan]
}
df = pd.DataFrame(data)

# Checking for missing values
print("Missing values in DataFrame:")
print(df.isna())

# Filling missing values with a default value
df_filled = df.fillna("Unknown")
print("\nDataFrame after filling missing values:")
print(df_filled)

# Dropping rows with missing values
df_dropped = df.dropna()
print("\nDataFrame after dropping missing rows:")
print(df_dropped)
