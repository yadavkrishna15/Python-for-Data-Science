import pandas as pd

print("NAME: KRISHNA YADAV")
print("ROLL NO: S124")
print()

# Read employee salary dataset
df = pd.read_csv("employee_salary.csv")

# 1. Display dataset
print("Employee Salary Dataset:")
print(df)

# 2. Display first 10 records
print("\nFirst 10 Records:")
print(df.head(10))

# 3. Find number of employees
print("\nNumber of Employees:")
print(len(df))

# 4. Display column names
print("\nColumn Names:")
print(df.columns)

# 5. Find average salary
print("\nAverage Salary:")
print(df["Salary"].mean())

# 6. Find average experience
print("\nAverage Experience:")
print(df["Experience"].mean())
