class Vehicle:
    def __init__(self, hours):
        self.hours = hours

    def calculate_charge(self):
        return 0.0


class Bike(Vehicle):
    def calculate_charge(self):
        return 10 * self.hours


class Car(Vehicle):
    def calculate_charge(self):
        return 30 + 20 * (self.hours - 1)


class Truck(Vehicle):
    def calculate_charge(self):
        return max(50 * self.hours, 100)


VEHICLE_TYPES = {
    "BIKE": Bike,
    "CAR": Car,
    "TRUCK": Truck
}

n = int(input())
total = 0.0

for _ in range(n):
    vehicle_type, hours = input().split()
    vehicle = VEHICLE_TYPES[vehicle_type](int(hours))

    charge = vehicle.calculate_charge()
    print(f"{vehicle_type}: {charge:.2f}")
    total += charge

print(f"Total: {total:.2f}")