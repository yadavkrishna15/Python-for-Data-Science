print("Squares from 1 to 10:")
for i in range(1, 11):
    print(i, "x", i, "=", i ** 2)

count = 0
for i in range(5):
    n = int(input("Enter number: "))
    if n % 2 == 0:
        count += 1

print("Even numbers count:", count)
