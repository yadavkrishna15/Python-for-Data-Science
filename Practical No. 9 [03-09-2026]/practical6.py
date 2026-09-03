import pandas as pd

print("NAME: KRISHNA YADAV")
print("ROLL NO: S124")
print()

# Read employee salary dataset
df = pd.read_csv("employee_salary.csv")

# Create Salary Category column
def salary_category(salary):
    if salary >= 7000:
        return "High"
    elif salary >= 5000:
        return "Medium"
    else:
        return "Low"

# Apply Salary Category function
df["Salary_Category"] = df["Salary"].apply(salary_category)


# Create Employee Level column
def employee_level(experience):
    if experience >= 8:
        return "Senior"
    elif experience >= 4:
        return "Mid-Level"
    else:
        return "Junior"

# Apply Employee Level function
df["Employee_Level"] = df["Experience"].apply(employee_level)

# Display updated dataset
print("Employee Dataset with New Columns:")
print(df)
