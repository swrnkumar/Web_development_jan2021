import sys

# try and except

try:
    x = int(input("Enter a value for x: "))
    y = int(input("Enter a value for y: "))
except ValueError:
    print("Error, invalid input!")
    sys.exit(1)    

try:
    result = x / y
except ZeroDivisionError:
    print("Error, division by zero!")
    sys.exit(1)

print(f"The result of {x} divided by {y} is {result}")
