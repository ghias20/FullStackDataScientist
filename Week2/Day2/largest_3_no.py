a, b, c = map(int, input("Enter 3 numbers: ").split())
largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c
print("Largest number is:", largest)
