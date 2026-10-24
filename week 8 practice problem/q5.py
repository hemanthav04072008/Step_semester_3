class Transport:
    def __init__(self, distance):
        self.distance = distance

    def calculate_fare(self):
        return 0.0


class Bus(Transport):
    def calculate_fare(self):
        return min(2 + (0.10 * self.distance), 10)


class Train(Transport):
    def calculate_fare(self):
        return 3 + (0.15 * self.distance)


class Metro(Transport):
    def __init__(self, distance, peak_hour_factor):
        super().__init__(distance)
        self.peak_hour_factor = peak_hour_factor

    def calculate_fare(self):
        base_fare = 1.50 + (0.20 * self.distance)
        return base_fare * self.peak_hour_factor


TRANSPORT_TYPES = {
    "BUS": Bus,
    "TRAIN": Train,
    "METRO": Metro
}

n = int(input())
total = 0.0

for _ in range(n):
    parts = input().split()
    transport_type = parts[0]
    distance = float(parts[1])

    if transport_type == "METRO":
        factor = float(parts[2])
        transport = TRANSPORT_TYPES[transport_type](distance, factor)
    else:
        transport = TRANSPORT_TYPES[transport_type](distance)

    fare = transport.calculate_fare()
    print(f"{transport_type}: {fare:.2f}")
    total += fare

print(f"Total: {total:.2f}")