from abc import ABC, abstractmethod

class Ticket(ABC):
    CONVENIENCE_FEE = 20

    def __init__(self, count):
        self.count = count

    @abstractmethod
    def calculate_amount(self):
        pass

    def total_amount(self):
        return (self.calculate_amount() + self.CONVENIENCE_FEE) * self.count

class Regular(Ticket):
    def calculate_amount(self):
        return 150

class Premium(Ticket):
    def calculate_amount(self):
        return 250

class Recliner(Ticket):
    def calculate_amount(self):
        return 400

n = int(input())
total = 0

for _ in range(n):
    seat, count = input().split()
    count = int(count)

    if seat == "REGULAR":
        ticket = Regular(count)
    elif seat == "PREMIUM":
        ticket = Premium(count)
    else:
        ticket = Recliner(count)

    amount = ticket.total_amount()
    print(f"{seat}: {amount:.2f}")
    total += amount

print(f"Total: {total:.2f}")