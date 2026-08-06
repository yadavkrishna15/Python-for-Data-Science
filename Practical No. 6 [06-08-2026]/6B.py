import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Customized line plot
plt.plot(x, y, color='red', linestyle='--', marker='o')

# Title and labels
plt.title("Customized Line Plot")
plt.xlabel("Numbers")
plt.ylabel("Doubles")

# Show the plot
plt.show()
