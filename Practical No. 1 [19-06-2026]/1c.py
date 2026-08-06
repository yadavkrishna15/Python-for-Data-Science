import math

while True:
    n = input("Enter a number (or 'q' to quit): ")
    if n == 'q':
        break
    try:
        print("Square root =", math.sqrt(float(n)))
    except ValueError:
        print("Invalid input!")
