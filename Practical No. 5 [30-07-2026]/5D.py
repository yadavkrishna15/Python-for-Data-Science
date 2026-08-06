print("KRISHNA YADAV S124")

import pandas as pd

# Creating Series
marks = pd.Series([85, 90, 78, 88, 95])

# Filtering values greater than 85
result = marks[marks > 85]

print("Marks greater than 85:")
print(result)
