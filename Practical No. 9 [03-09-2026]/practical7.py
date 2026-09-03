import pandas as pd

print("NAME: KRISHNA YADAV")
print("ROLL NO: S124")
print()

# Read employee salary dataset
df = pd.read_csv("employee_salary.csv")

# 1. Average Salary
print("Average Salary:", df["Salary"].mean())

# 2. Maximum Salary
print("Maximum Salary:", df["Salary"].max())

# 3. Minimum Salary
print("Minimum Salary:", df["Salary"].min())

# 4. Median Salary
print("Median Salary:", df["Salary"].median())

# 5. Standard Deviation of Salary
print("Standard Deviation of Salary:", df["Salary"].std())

# 6. Average Experience
print("Average Experience:", df["Experience"].mean())

# 7. Number of Employees
print("Number of Employees:", df["Name"].count())

# 8. Employees earning above 5000
print("Employees earning above 5000:",
      (df["Salary"] > 5000).sum())
