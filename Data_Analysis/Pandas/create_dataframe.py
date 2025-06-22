# create_dataframe.py
import pandas as pd

# Creating a DataFrame from a list
data = [10, 20, 30, 40]
df_from_list = pd.DataFrame(data, columns=['Values'])
print("DataFrame from list:")
print(df_from_list)

# Creating a DataFrame from a dictionary
data_dict = {
    'Name': ['John', 'Jane', 'Jack'],
    'Age': [28, 24, 30]
}
df_from_dict = pd.DataFrame(data_dict)
print("\nDataFrame from dictionary:")
print(df_from_dict)
