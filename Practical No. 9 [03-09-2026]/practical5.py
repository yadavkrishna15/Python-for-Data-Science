import pandas as pd

print("NAME: KRISHNA YADAV")
print("ROLL NO: S124")
print()

# Read employee salary dataset
df = pd.read_csv("employee_salary.csv")

# Create missing values for demonstration
df.loc[2, "Salary"] = None
df.loc[5, "Experience"] = None

# Display dataset with missing values
print("Dataset with Missing Values:")
print(df)

# 1. Identify missing values
print("\nMissing Values:")
print(df.isnull())

# 2. Count missing values in each column
print("\nCount of Missing Values:")
print(df.isnull().sum())

# 3. Replace missing salary with average salary
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# 4. Replace missing experience with average experience
df["Experience"] = df["Experience"].fillna(df["Experience"].mean())

# 5. Display cleaned dataset
print("\nCleaned Dataset:")
print(df)
