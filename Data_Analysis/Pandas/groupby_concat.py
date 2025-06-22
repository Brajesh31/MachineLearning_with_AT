# groupby_concat.py
import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['John', 'Jane', 'Jack', 'Jill'],
    'Department': ['HR', 'IT', 'HR', 'IT'],
    'Salary': [50000, 60000, 55000, 65000]
}
df = pd.DataFrame(data)

# Grouping by department and calculating average salary
grouped = df.groupby('Department').mean()
print("Average salary by department:")
print(grouped)

# Concatenating two DataFrames
data2 = {
    'Name': ['Jake', 'Laura'],
    'Department': ['HR', 'IT'],
    'Salary': [48000, 62000]
}
df2 = pd.DataFrame(data2)

df_concat = pd.concat([df, df2])
print("\nConcatenated DataFrame:")
print(df_concat)
