# Question 1: Tuple Operations

# a. Create a tuple with 5 different elements and print it
subjects = ("Machine Learning", "DBMS", "AI", "Cloud Computing", "Cyber Security")
print("a. Tuple:", subjects)

# b. Access the first and last elements using indexing
print("\nb. First Element:", subjects[0])
print("Last Element:", subjects[-1])

# c. Slice a tuple and print the middle 3 elements
print("\nc. Middle 3 Elements:", subjects[1:4])

# d. Concatenate two tuples and print the result
more_subjects = ("Data Mining", "Big Data")
concatenated_tuple = subjects + more_subjects
print("\nd. Concatenated Tuple:", concatenated_tuple)

# e. Reverse a tuple using slicing
reversed_tuple = subjects[::-1]
print("\ne. Reversed Tuple:", reversed_tuple)

# f. Count how many times an element appears in a tuple
numbers = (10, 20, 30, 20, 40, 20, 50)
count_20 = numbers.count(20)
print("\nf. Count of 20:", count_20)

# g. Find the index of a specific element in a tuple
index_ai = subjects.index("AI")
print("\ng. Index of 'AI':", index_ai)

# h. Check if an element exists in a tuple
element = "DBMS"
if element in subjects:
    print("\nh. Element exists in tuple.")
else:
    print("\nh. Element does not exist in tuple.")

# i. Convert a list to a tuple
subject_list = ["Python", "Java", "C++", "Scala"]
subject_tuple = tuple(subject_list)
print("\ni. Tuple from List:", subject_tuple)

# j. Sort a tuple of numbers in ascending order
num_tuple = (45, 12, 78, 34, 23)
sorted_tuple = tuple(sorted(num_tuple))
print("\nj. Sorted Tuple:", sorted_tuple)

# k. Repeat a tuple 3 times using * operator
repeated_tuple = ("Python", "AI") * 3
print("\nk. Repeated Tuple:", repeated_tuple)

# l. Check immutability property of tuples
immutable_tuple = ("ML", 401)

try:
    immutable_tuple[1] = 999
except TypeError as e:
    print("\nl. Tuple is immutable!")
    print("Error:", e)
