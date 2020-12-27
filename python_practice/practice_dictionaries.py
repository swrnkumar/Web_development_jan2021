houses = {"Sion": "Laan van Sion", "Parkrijk": "Beemdgrasstraat"}
houses["Haarnaspolder"] = "van der mareltuin"
print(houses["Parkrijk"])
print(houses["Sion"])
print(houses)

# functions practice
def square(x):
    return x * x

for i in range(10):
    print(f"The square of {i} is {square(i)}")