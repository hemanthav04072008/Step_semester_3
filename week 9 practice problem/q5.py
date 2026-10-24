class Appliance:
    POWER = 0

    def __init__(self, hours):
        self.hours = hours

    def calculate_units(self, saver=False):
        if saver:
            return None

        return self.POWER * self.hours / 1000


class Fridge(Appliance):
    POWER = 150


class TV(Appliance):
    POWER = 100


class SaverAppliance(Appliance):
    def calculate_units(self, saver=False):
        units = self.POWER * self.hours / 1000

        if saver:
            units *= 0.75

        return units


class AirConditioner(SaverAppliance):
    POWER = 1500


class Washer(SaverAppliance):
    POWER = 500


appliance_types = {
    "FRIDGE": Fridge,
    "AC": AirConditioner,
    "TV": TV,
    "WASHER": Washer
}

n = int(input())
total_cost = 0.0

for _ in range(n):
    parts = input().split()

    appliance_type = parts[0]
    hours = float(parts[1])
    saver = len(parts) == 3 and parts[2] == "SAVER"

    appliance = appliance_types[appliance_type](hours)
    units = appliance.calculate_units(saver)

    if units is None:
        print(f"{appliance_type}: saver mode not supported")
        continue

    cost = units * 8
    print(
        f"{appliance_type}: Units={units:.2f} "
        f"Cost={cost:.2f}"
    )

    total_cost += cost

print(f"Total Cost: {total_cost:.2f}")