class Cab:
    def __init__(self, km):
        self.km = km

    def rate_per_km(self):
        raise NotImplementedError

    def night_service_fare(self, fare):
        return None

    def calculate_fare(self, time):
        fare = max(self.km * self.rate_per_km(), 100)

        if time == "NIGHT":
            return self.night_service_fare(fare)

        return fare


class Mini(Cab):
    def rate_per_km(self):
        return 10


class Sedan(Cab):
    def rate_per_km(self):
        return 14

    def night_service_fare(self, fare):
        return fare * 1.20


class SUV(Cab):
    def rate_per_km(self):
        return 18

    def night_service_fare(self, fare):
        return fare * 1.20


cab_types = {
    "MINI": Mini,
    "SEDAN": Sedan,
    "SUV": SUV
}

n = int(input())
total = 0.0

for _ in range(n):
    cab_type, km, time = input().split()
    cab = cab_types[cab_type](float(km))

    fare = cab.calculate_fare(time)

    if fare is None:
        print(f"{cab_type}: night service not available")
    else:
        print(f"{cab_type}: {fare:.2f}")
        total += fare

print(f"Total: {total:.2f}")