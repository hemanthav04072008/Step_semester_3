class Transport:
    def __init__(self, distance):
        self.distance = distance

    def calculate_fare(self):
        pass


class Bus(Transport):
    def calculate_fare(self):
        fare = 2 + (0.10 * self.distance)

        if fare > 10:
            fare = 10

        return fare


class Train(Transport):
    def calculate_fare(self):
        return 3 + (0.15 * self.distance)


class Metro(Transport):
    def __init__(self, distance, peak_factor):
        super().__init__(distance)
        self.peak_factor = peak_factor

    def calculate_fare(self):
        return (1.50 + (0.20 * self.distance)) * self.peak_factor


n = int(input())
total = 0

for i in range(n):
    data = input().split()

    transport_type = data[0]
    distance = float(data[1])

    if transport_type == "BUS":
        transport = Bus(distance)

    elif transport_type == "TRAIN":
        transport = Train(distance)

    else:
        peak_factor = float(data[2])
        transport = Metro(distance, peak_factor)

    fare = transport.calculate_fare()
    total += fare

    print(f"{transport_type}: {fare:.2f}")

print(f"Total: {total:.2f}")