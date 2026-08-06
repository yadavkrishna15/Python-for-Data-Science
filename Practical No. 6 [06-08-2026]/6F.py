import matplotlib.pyplot as plt

# Data
x = [5, 7, 8, 7, 6, 9, 5]
y = [99, 86, 87, 88, 100, 86, 103]

# Create scatter plot
plt.scatter(x, y, color='green', s=100)

# Add title and labels
plt.title("Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

# Display the plot
plt.show()
