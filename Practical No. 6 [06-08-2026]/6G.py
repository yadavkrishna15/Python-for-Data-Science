import matplotlib.pyplot as plt
import numpy as np

# Generate 100 random numbers from a normal distribution
data = np.random.normal(0, 1, 100)

# Create histogram with 20 bins
plt.hist(data, bins=20)

# Add title and labels
plt.title("Histogram of Random Numbers")
plt.xlabel("Value")
plt.ylabel("Frequency")

# Add grid
plt.grid(True)

# Display the plot
plt.show()
