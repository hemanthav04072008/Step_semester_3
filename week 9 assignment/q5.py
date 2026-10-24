from abc import ABC, abstractmethod


class TravelBooking(ABC):
    BOOKING_FEE = 50

    def __init__(self, distance):
        self.distance = distance

    @abstractmethod
    def calculate_base_fare(self):
        pass

    def calculate_total(self):
        return self.calculate_base_fare() + TravelBooking.BOOKING_FEE


class Bus(TravelBooking):
    def calculate_base_fare(self):
        return self.distance * 2


class Train(TravelBooking):
    def calculate_base_fare(self):
        return self.distance * 1.5


class Flight(TravelBooking):
    def calculate_base_fare(self):
        return 2500 + self.distance * 4


travel_types = {
    "BUS": Bus,
    "TRAIN": Train,
    "FLIGHT": Flight
}

n = int(input())

for _ in range(n):
    mode, distance = input().split()

    booking = travel_types[mode](float(distance))
    total = booking.calculate_total()

    print(f"{mode}: {total:.2f}")