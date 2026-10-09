from abc import ABC, abstractmethod

BOOKING_FEE = 50

class Travel(ABC):
    def __init__(self, distance):
        self.distance = distance

    @abstractmethod
    def calculate_fare(self):
        pass

    def total_fare(self):
        return self.calculate_fare() + BOOKING_FEE

class Bus(Travel):
    def calculate_fare(self):
        return self.distance * 2

class Train(Travel):
    def calculate_fare(self):
        return self.distance * 1.5

class Flight(Travel):
    def calculate_fare(self):
        return 2500 + self.distance * 4

n = int(input())
bookings = []

for _ in range(n):
    data = input().split()
    mode = data[0]
    distance = float(data[1])

    if mode == "BUS":
        bookings.append(("BUS", Bus(distance)))
    elif mode == "TRAIN":
        bookings.append(("TRAIN", Train(distance)))
    elif mode == "FLIGHT":
        bookings.append(("FLIGHT", Flight(distance)))

for mode, booking in bookings:
    print(f"{mode}: {booking.total_fare():.2f}")