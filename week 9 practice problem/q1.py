from abc import ABC, abstractmethod


class Ticket(ABC):
    CONVENIENCE_FEE = 20

    def __init__(self, count):
        self.count = count

    @abstractmethod
    def price_per_ticket(self):
        pass

    def calculate_amount(self):
        return self.count * (
            self.price_per_ticket() + Ticket.CONVENIENCE_FEE
        )


class RegularTicket(Ticket):
    def price_per_ticket(self):
        return 150


class PremiumTicket(Ticket):
    def price_per_ticket(self):
        return 250


class ReclinerTicket(Ticket):
    def price_per_ticket(self):
        return 400


ticket_types = {
    "REGULAR": RegularTicket,
    "PREMIUM": PremiumTicket,
    "RECLINER": ReclinerTicket
}

n = int(input())
total = 0.0

for _ in range(n):
    seat, count = input().split()
    ticket = ticket_types[seat](int(count))

    amount = ticket.calculate_amount()
    print(f"{seat}: {amount:.2f}")
    total += amount

print(f"Total: {total:.2f}")