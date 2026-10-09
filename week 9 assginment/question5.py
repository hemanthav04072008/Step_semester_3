from abc import ABC, abstractmethod

class Appliance(ABC):
    RATE = 8

    def __init__(self, hours):
        self.hours = hours

    @abstractmethod
    def power(self):
        pass

    def supports_saver(self):
        return False

    def calculate_units(self, saver=False):
        units = self.power() * self.hours / 1000

        if saver and self.supports_saver():
            units *= 0.75

        return units

    def calculate_cost(self, saver=False):
        return self.calculate_units(saver) * self.RATE

class Fridge(Appliance):
    def power(self):
        return 150

class AC(Appliance):
    def power(self):
        return 1500

    def supports_saver(self):
        return True

class TV(Appliance):
    def power(self):
        return 100

class Washer(Appliance):
    def power(self):
        return 500

    def supports_saver(self):
        return True

n = int(input())
total_cost = 0

for _ in range(n):
    data = input().split()
    appliance_type = data[0]
    hours = float(data[1])
    saver = len(data) == 3 and data[2] == "SAVER"

    if appliance_type == "FRIDGE":
        appliance = Fridge(hours)
    elif appliance_type == "AC":
        appliance = AC(hours)
    elif appliance_type == "TV":
        appliance = TV(hours)
    else:
        appliance = Washer(hours)

    if saver and not appliance.supports_saver():
        print(f"{appliance_type}: saver mode not supported")
        continue

    units = appliance.calculate_units(saver)
    cost = appliance.calculate_cost(saver)

    print(f"{appliance_type}: Units={units:.2f} Cost={cost:.2f}")
    total_cost += cost

print(f"Total Cost: {total_cost:.2f}")