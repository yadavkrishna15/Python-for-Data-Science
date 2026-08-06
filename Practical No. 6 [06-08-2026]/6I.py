import matplotlib.pyplot as plt
import numpy as np

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

categories = ["DS", "Scala", "OS", "Python"]
scores = [65, 70, 74, 60]

scatter_x = [5, 7, 8, 7, 6, 9, 5]
scatter_y = [99, 86, 87, 88, 100, 86, 103]

hist_data = np.random.normal(0, 1, 100)

# Create 2x2 grid of subplots
plt.figure(figsize=(10, 8))

# Top-left: Line Plot
plt.subplot(2, 2, 1)
plt.plot(x, y, marker='o')
plt.title("Line Plot")

# Top-right: Bar Chart
plt.subplot(2, 2, 2)
plt.bar(categories, scores)
plt.title("Bar Chart")

# Bottom-left: Scatter Plot
plt.subplot(2, 2, 3)
plt.scatter(scatter_x, scatter_y, color='green', s=100)
plt.title("Scatter Plot")

# Bottom-right: Histogram
plt.subplot(2, 2, 4)
plt.hist(hist_data, bins=20)
plt.title("Histogram")

# Adjust layout
plt.tight_layout()

# Display all plots
plt.show()
