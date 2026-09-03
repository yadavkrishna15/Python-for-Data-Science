import pandas as pd

print("NAME: KRISHNA YADAV")
print("ROLL NO: S124")
print()

# Read employee salary dataset
df = pd.read_csv("employee_salary.csv")

# 1. Sort employees by salary in ascending order
print("Salary in Ascending Order:")
print(df.sort_values("Salary"))

# 2. Sort employees by salary in descending order
print("\nSalary in Descending Order:")
print(df.sort_values("Salary", ascending=False))

# 3. Sort employees by experience in descending order
print("\nExperience in Descending Order:")
print(df.sort_values("Experience", ascending=False))

# 4. Display top 5 highest paid employees
print("\nTop 5 Highest Paid Employees:")
print(df.sort_values("Salary", ascending=False).head(5))

# 5. Display bottom 3 lowest paid employees
print("\nBottom 3 Lowest Paid Employees:")
print(df.sort_values("Salary").head(3))
