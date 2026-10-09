class Vehicle:
    def __init__(self, hours):
        self.hours = hours

    def calculate_charge(self):
        pass


class Bike(Vehicle):
    def calculate_charge(self):
        return self.hours * 10


class Car(Vehicle):
    def calculate_charge(self):
        if self.hours == 1:
            return 30
        return 30 + (self.hours - 1) * 20


class Truck(Vehicle):
    def calculate_charge(self):
        charge = self.hours * 50

        if charge < 100:
            charge = 100

        return charge


n = int(input())
total = 0

for i in range(n):
    vehicle_type, hours = input().split()
    hours = int(hours)

    if vehicle_type == "BIKE":
        vehicle = Bike(hours)
    elif vehicle_type == "CAR":
        vehicle = Car(hours)
    else:
        vehicle = Truck(hours)

    charge = vehicle.calculate_charge()
    total += charge

    print(f"{vehicle_type}: {charge:.2f}")

print(f"Total: {total:.2f}")