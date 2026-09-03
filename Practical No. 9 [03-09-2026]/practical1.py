import pandas as pd

# Read employee salary dataset
df = pd.read_csv("employee_salary.csv")

# 1. Display complete dataset
print("Complete Dataset:")
print(df)

# 2. Display first 5 records
print("\nFirst 5 Records:")
print(df.head())

# 3. Display last 5 records
print("\nLast 5 Records:")
print(df.tail())

# 4. Display number of rows and columns
print("\nNumber of Rows and Columns:")
print(df.shape)

# 5. Display column names
print("\nColumn Names:")
print(df.columns)

# 6. Display basic information
print("\nDataset Information:")
df.info()

# 7. Display statistical information
print("\nStatistical Information:")
print(df.describe())
