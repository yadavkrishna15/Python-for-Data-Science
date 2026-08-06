students = {
    "MrBeast": 95,
    "Karl": 88,
    "Chandler": 72,
    "Chris": 85,
    "Jimmy": 91
}

print("Student Marks:")
for name, marks in students.items():
    print(name, ":", marks)

average = sum(students.values()) / len(students)
print("\nClass Average:", average)

topper = max(students, key=students.get)
print("Highest Marks:", topper, "with", students[topper], "marks")
