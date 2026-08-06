print("KRISHNA YADAV S124")
import pandas as pd

# Creating a DataFrame
data = {
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 78, 88, 95]
}

df = pd.DataFrame(data)

print("Statistical Information:")
print(df.describe())
