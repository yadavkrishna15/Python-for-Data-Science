import numpy as np

# ---------- 4a. Create a NumPy Array ----------
print("----- 4a: Create a NumPy Array -----")
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)
print("Type:", type(arr))

# ---------- 4b. Basic Operations on a Single Array ----------
print("\n----- 4b: Basic Operations on Single Array -----")
print("Array:", arr)
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))
print("Standard Deviation:", np.std(arr))
print("Add 5:", arr + 5)
print("Multiply by 2:", arr * 2)
print("Square:", arr ** 2)

# ---------- 4c. Create Array of 10 Elements and Slice 1st to 5th ----------
print("\n----- 4c: Create Array (10 elements) and Slice -----")
arr10 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Original Array:", arr10)
sliced = arr10[0:5]
print("Sliced (1st to 5th element):", sliced)

# ---------- 4d. Sort an Array Alphabetically ----------
print("\n----- 4d: Sort Array Alphabetically -----")
str_arr = np.array(["Banana", "Apple", "Mango", "Cherry", "Date"])
sorted_arr = np.sort(str_arr)
print("Original Array:", str_arr)
print("Sorted Array:", sorted_arr)

# ---------- 4e. Filter Array to Return Maximum Value(s) ----------
print("\n----- 4e: Filter Array for Maximum Value(s) -----")
num_arr = np.array([12, 45, 7, 89, 34, 89, 23])
max_value = np.max(num_arr)
filter_arr = num_arr == max_value
result = num_arr[filter_arr]
print("Original Array:", num_arr)
print("Filter Array:", filter_arr)
print("Maximum Value(s):", result)

print("KRISHNA YADAV S124")
