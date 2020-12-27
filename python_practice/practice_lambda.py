# practice lambda functions

people = [
    {"name": "Harry", "country": "UK"},
    {"name": "Akash", "country": "India"},
    {"name": "Sara", "country": "Qatar"},
    {"name": "Matt", "country": "New Zealand"},
    {"name": "Stephen", "country": "Canada"}
]

def f(person):
    return person["name"]

people.sort(key=f)

print(people)

# same code using lambda function

people.sort(key = lambda person: person["country"])
print(people)