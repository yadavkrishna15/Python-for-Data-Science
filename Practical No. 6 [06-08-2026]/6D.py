import matplotlib.pyplot as plt

# Data
categories = ["Data Structures", "Scala for DS", "Operating System", "Python for DS"]
scores = [65, 70, 74, 60]

# Create horizontal bar chart
plt.barh(categories, scores)

# Add title and labels
plt.title("Student Scores")
plt.xlabel("Scores")
plt.ylabel("Subjects")

# Display the chart
plt.show()
