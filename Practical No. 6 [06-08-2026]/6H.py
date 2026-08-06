import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 4, 9, 16, 25]

# Create first subplot
plt.subplot(1, 2, 1)
plt.plot(x, y1, marker='o')
plt.title("Line Plot")

# Create second subplot
plt.subplot(1, 2, 2)
plt.bar(x, y2)
plt.title("Bar Chart")

# Adjust layout
plt.tight_layout()

# Display the figure
plt.show()
