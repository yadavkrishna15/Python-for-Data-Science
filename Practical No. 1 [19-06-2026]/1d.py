def swap_elements(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]
    return lst

numbers = list(map(int, input("Enter list elements separated by spaces: ").split()))
i = int(input("Enter first index: "))
j = int(input("Enter second index: "))

swap_elements(numbers, i, j)
print("Updated list:", numbers)
