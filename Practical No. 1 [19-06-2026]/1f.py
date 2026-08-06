numbers = [45, 12, 78, 34, 89, 23, 56, 67, 11, 90]

print("Original List:", numbers)
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Average:", sum(numbers) / len(numbers))

numbers.sort()
print("Ascending Order:", numbers)

numbers.sort(reverse=True)
print("Descending Order:", numbers)

numbers.append(100)
print("After Adding 100:", numbers)

numbers.pop(0)
print("After Removing First Item:", numbers)
