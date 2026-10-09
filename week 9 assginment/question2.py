from abc import ABC, abstractmethod

class Parcel(ABC):
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    @abstractmethod
    def calculate_charge(self):
        pass

    def calculate_insurance(self):
        return 0

    def calculate_total(self):
        return self.calculate_charge() + self.calculate_insurance()

class Standard(Parcel):
    def calculate_charge(self):
        return 40 + 10 * self.weight

class Express(Parcel):
    def calculate_charge(self):
        return 80 + 15 * self.weight

    def calculate_insurance(self):
        return 0.02 * self.value

class Fragile(Parcel):
    def calculate_charge(self):
        return 40 + 10 * self.weight + 50

    def calculate_insurance(self):
        return 0.02 * self.value

n = int(input())
grand_total = 0

for _ in range(n):
    data = input().split()
    parcel_type = data[0]
    weight = float(data[1])
    value = float(data[2])

    if parcel_type == "STANDARD":
        parcel = Standard(weight, value)
    elif parcel_type == "EXPRESS":
        parcel = Express(weight, value)
    else:
        parcel = Fragile(weight, value)

    charge = parcel.calculate_charge()
    insurance = parcel.calculate_insurance()
    total = parcel.calculate_total()

    print(
        f"{parcel_type}: Charge={charge:.2f} "
        f"Insurance={insurance:.2f} Total={total:.2f}"
    )
    grand_total += total

print(f"Grand Total: {grand_total:.2f}")