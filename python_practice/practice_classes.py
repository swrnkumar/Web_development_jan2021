class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

p = Point(345,876)
print(p.x)
print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers)

flightA = Flight(5)

people = ["Harry", "Larry", "Lara", "Sara", "Pete", "Matt"]

for person in people:
    if flightA.add_passenger(person):
        print(f"The person {person} was added to flight")
    else:
        print(f"NO available seats on flight for {person}")


# decorators practice
