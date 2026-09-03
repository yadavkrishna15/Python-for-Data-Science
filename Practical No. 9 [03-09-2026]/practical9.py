import pandas as pd
import matplotlib.pyplot as plt

print("NAME: KRISHNA YADAV")
print("ROLL NO: S124")
print()

# Read employee salary dataset
df = pd.read_csv("employee_salary.csv")

# 1. Bar Chart
plt.figure(figsize=(10, 5))
plt.bar(df["Name"], df["Salary"])
plt.xlabel("Employee Name")
plt.ylabel("Salary")
plt.title("Employee Name vs Salary - Bar Chart")
plt.xticks(rotation=45)
plt.show()


# 2. Line Chart
plt.figure(figsize=(10, 5))
plt.plot(df["Name"], df["Salary"], marker="o")
plt.xlabel("Employee Name")
plt.ylabel("Salary")
plt.title("Employee Name vs Salary - Line Chart")
plt.xticks(rotation=45)
plt.show()


# 3. Histogram
plt.figure(figsize=(8, 5))
plt.hist(df["Salary"], bins=5)
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.title("Distribution of Employee Salary")
plt.show()


# 4. Pie Chart
department_count = df["Department"].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(
    department_count,
    labels=department_count.index,
    autopct="%1.1f%%"
)

plt.title("Employees by Department")
plt.show()
