# Original nested tuple of subjects

nested_tuple = (
    ("Machine Learning", 401),
    ("Database Management System", 405),
    ("Artificial Intelligence", 403)
)

# Sorting the nested tuple by subject code (index 1)

sorted_subjects = sorted(nested_tuple, key=lambda x: x[1])

# Display the sorted result

print("Sorted Subjects (by subject code):", sorted_subjects)
