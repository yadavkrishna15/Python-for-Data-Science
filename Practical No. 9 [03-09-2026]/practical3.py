import pandas as pd

print("NAME: KRISHNA YADAV")
print("ROLL NO: S124")
print()

# Read employee salary dataset
df = pd.read_csv("employee_salary.csv")

# 1. Display Name and Salary
print("Employee Name and Salary:")
print(df[["Name", "Salary"]])

# 2. Employees with salary greater than 5000
print("\nEmployees with Salary Greater Than 5000:")
print(df[df["Salary"] > 5000])

# 3. Employees with experience greater than 5 years
print("\nEmployees with Experience Greater Than 5 Years:")
print(df[df["Experience"] > 5])

# 4. Female employees
print("\nFemale Employees:")
print(df[df["Gender"] == "Female"])

# 5. IT department employees
print("\nIT Department Employees:")
print(df[df["Department"] == "IT"])

# 6. Employees with Salary > 5000 and Experience > 5
print("\nEmployees with Salary > 5000 and Experience > 5:")
print(df[(df["Salary"] > 5000) & (df["Experience"] > 5)])
