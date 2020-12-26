print("Hello world!")
name = input("Enter your name:")
print(f"Hello, {name}")

#conditions
n = int(input("Enter a number: "))
if n > 0:
    print("The number  n  is positive ")
elif n < 0:
    print("The number n  is negative")
else:
    print("The number is zero")

#sequences, lists practice
nameH = "Harry"
print(nameH[0])
names1 = ["Harry", "Leo", "Sarah", "Lara"]

names1.append("Matt")

names1.sort()

print(names1)

# practice sets

s = set()

s.add(3)
s.add(456)
s.add(-1)
s.add(3)
s.remove(3)
print(s)

print(f"The number of elements in the set is {len(s)} ")
print(f"The number of elements in the list is {len(names1)}")