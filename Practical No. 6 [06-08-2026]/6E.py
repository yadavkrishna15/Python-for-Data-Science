import matplotlib.pyplot as plt

# Data
categories = ["Data Structures", "Scala for DS", "Operating System", "Python for DS"]
scores = [65, 70, 74, 60]

# Explode the "Python for DS" slice
explode = (0, 0, 0, 0.1)

# Create pie chart
plt.pie(scores,
        labels=categories,
        autopct='%1.1f%%',
        explode=explode)

# Add title
plt.title("Student Scores")

# Display the chart
plt.show()
