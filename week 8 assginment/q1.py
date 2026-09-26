class Customer:
    def __init__(self, amount):
        self.amount = amount

    def calculate_amount(self):
        pass


class Student(Customer):
    def calculate_amount(self):
        return self.amount * 0.90


class Staff(Customer):
    def calculate_amount(self):
        return self.amount * 0.95


class Guest(Customer):
    def calculate_amount(self):
        return self.amount + 10


n = int(input())
total = 0

for i in range(n):
    customer_type, amount = input().split()
    amount = float(amount)

    if customer_type == "STUDENT":
        customer = Student(amount)
    elif customer_type == "STAFF":
        customer = Staff(amount)
    else:
        customer = Guest(amount)

    final_amount = customer.calculate_amount()
    total += final_amount

    print(f"{customer_type}: {final_amount:.2f}")

print(f"Total: {total:.2f}")