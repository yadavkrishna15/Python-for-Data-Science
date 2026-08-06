# Question 2: List Operations

# a. Find the largest number in a list
numbers = [25, 67, 12, 89, 45]
largest = max(numbers)
print("a. Largest Number:", largest)

# b. Remove duplicates from a list
duplicate_list = [10, 20, 30, 20, 40, 10, 50]
unique_list = list(set(duplicate_list))
print("\nb. List after removing duplicates:", unique_list)

# c. Count how many even numbers are in a list
num_list = [1, 2, 3, 4, 5, 6, 8, 10]
even_count = 0

for num in num_list:
    if num % 2 == 0:
        even_count += 1

print("\nc. Number of even elements:", even_count)

# d. Input 5 numbers and store them in a list
input_list = []

print("\nd. Enter 5 numbers:")
for i in range(5):
    n = int(input(f"Enter number {i+1}: "))
    input_list.append(n)

print("Stored List:", input_list)

# e. Function to return the average of all numbers in a list
def calculate_average(lst):
    return sum(lst) / len(lst)

avg = calculate_average(numbers)
print("\ne. Average of numbers:", avg)

# f. Convert a string into a list of characters using list()
text = "Python"
char_list = list(text)
print("\nf. List of Characters:", char_list)

# g. Join all elements of a list into a single string using join()
words = ["Data", "Science", "with", "Python"]
joined_string = " ".join(words)
print("\ng. Joined String:", joined_string)
