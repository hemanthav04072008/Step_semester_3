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

n = int(input())
connections = []

for _ in range(n):
    data = input().split()
    connection_type = data[0]
    units = int(data[1])

    if connection_type == "HOME":
        connections.append(("HOME", Home(units)))
    elif connection_type == "SHOP":
        connections.append(("SHOP", Shop(units)))
    elif connection_type == "FACTORY":
        connections.append(("FACTORY", Factory(units)))

total = 0

for connection_type, connection in connections:
    bill = connection.calculate_bill()
    print(f"{connection_type}: {bill:.2f}")
    total += bill

print(f"Total: {total:.2f}")