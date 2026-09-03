import pandas as pd

print("NAME: KRISHNA YADAV")
print("ROLL NO: S124")
print()

# Read employee salary dataset
df = pd.read_csv("employee_salary.csv")

# 1. Number of employees in each department
print("Number of Employees in Each Department:")
print(df.groupby("Department")["Name"].count())

# 2. Average salary in each department
print("\nAverage Salary by Department:")
print(df.groupby("Department")["Salary"].mean())

# 3. Maximum salary in each department
print("\nMaximum Salary by Department:")
print(df.groupby("Department")["Salary"].max())

# 4. Average experience in each department
print("\nAverage Experience by Department:")
print(df.groupby("Department")["Experience"].mean())
