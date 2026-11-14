"""Demonstrate grouping and concatenating Pandas DataFrames."""
import pandas as pd

def main() -> None:
    employees = pd.DataFrame({
        "Name": ["John", "Jane", "Jack", "Jill"],
        "Department": ["HR", "IT", "HR", "IT"],
        "Salary": [50000, 60000, 55000, 65000],
    })
    average_salary = employees.groupby("Department")["Salary"].mean()
    print("Average salary by department:")
    print(average_salary)

    new_employees = pd.DataFrame({
        "Name": ["Jake", "Laura"],
        "Department": ["HR", "IT"],
        "Salary": [48000, 62000],
    })
    combined = pd.concat([employees, new_employees], ignore_index=True)
    print("\nConcatenated DataFrame:")
    print(combined)

if __name__ == "__main__":
    main()
