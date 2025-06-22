# csv_read_write.py
import pandas as pd

# Reading a CSV file
df = pd.read_csv('data.csv')
print("Data from CSV file:")
print(df)

# Writing to a CSV file
df.to_csv('output.csv', index=False)
print("\nData has been written to 'output.csv'.")
