from abc import ABC, abstractmethod

class Cab(ABC):
    def __init__(self, km):
        self.km = km

    @abstractmethod
    def calculate_fare(self):
        pass

    def final_fare(self, time):
        fare = max(self.calculate_fare(), 100)

        if time == "NIGHT":
            fare *= 1.20

        return fare

class Mini(Cab):
    def calculate_fare(self):
        return self.km * 10

class Sedan(Cab):
    def calculate_fare(self):
        return self.km * 14

class SUV(Cab):
    def calculate_fare(self):
        return self.km * 18

n = int(input())
total = 0

for _ in range(n):
    cab_type, km, time = input().split()
    km = float(km)

    if cab_type == "MINI" and time == "NIGHT":
        print("MINI: night service not available")
        continue

    if cab_type == "MINI":
        cab = Mini(km)
    elif cab_type == "SEDAN":
        cab = Sedan(km)
    else:
        cab = SUV(km)

    fare = cab.final_fare(time)
    print(f"{cab_type}: {fare:.2f}")
    total += fare

print(f"Total: {total:.2f}")