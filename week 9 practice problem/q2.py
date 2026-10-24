from abc import ABC, abstractmethod


class Parcel(ABC):
    def __init__(self, weight, declared_value):
        self.weight = weight
        self.declared_value = declared_value

    @abstractmethod
    def calculate_charge(self):
        pass

    def calculate_insurance(self):
        return 0.0

    def calculate_total(self):
        return self.calculate_charge() + self.calculate_insurance()


class StandardParcel(Parcel):
    def calculate_charge(self):
        return 40 + 10 * self.weight


class InsurableParcel(Parcel):
    def calculate_insurance(self):
        return self.declared_value * 0.02


class ExpressParcel(InsurableParcel):
    def calculate_charge(self):
        return 80 + 15 * self.weight


class FragileParcel(InsurableParcel):
    def calculate_charge(self):
        return 40 + 10 * self.weight + 50


parcel_types = {
    "STANDARD": StandardParcel,
    "EXPRESS": ExpressParcel,
    "FRAGILE": FragileParcel
}

n = int(input())
grand_total = 0.0

for _ in range(n):
    parcel_type, weight, declared_value = input().split()

    parcel = parcel_types[parcel_type](
        float(weight), float(declared_value)
    )

    charge = parcel.calculate_charge()
    insurance = parcel.calculate_insurance()
    total = parcel.calculate_total()

    print(
        f"{parcel_type}: Charge={charge:.2f} "
        f"Insurance={insurance:.2f} Total={total:.2f}"
    )

    grand_total += total

print(f"Grand Total: {grand_total:.2f}")