from abc import ABC, abstractmethod


class Connection(ABC):
    def __init__(self, units):
        self.units = units

    @abstractmethod
    def calculate_bill(self):
        pass


class Home(Connection):
    def calculate_bill(self):
        if self.units <= 100:
            return self.units * 5

        return 100 * 5 + (self.units - 100) * 7


class Shop(Connection):
    def calculate_bill(self):
        return self.units * 8 + 100


class Factory(Connection):
    def calculate_bill(self):
        return max(self.units * 6, 1000)


connection_types = {
    "HOME": Home,
    "SHOP": Shop,
    "FACTORY": Factory
}

n = int(input())
total = 0.0

for _ in range(n):
    connection_type, units = input().split()

    connection = connection_types[connection_type](int(units))
    bill = connection.calculate_bill()

    print(f"{connection_type}: {bill:.2f}")
    total += bill

print(f"Total: {total:.2f}")