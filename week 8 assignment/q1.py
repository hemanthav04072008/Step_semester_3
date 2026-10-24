class CustomerBill:
    def __init__(self, amount):
        self.amount = amount

    def final_amount(self):
        return self.amount


class StudentBill(CustomerBill):
    def final_amount(self):
        return self.amount * 0.90


class StaffBill(CustomerBill):
    def final_amount(self):
        return self.amount * 0.95


class GuestBill(CustomerBill):
    def final_amount(self):
        return self.amount + 10


CUSTOMER_TYPES = {
    "STUDENT": StudentBill,
    "STAFF": StaffBill,
    "GUEST": GuestBill
}

n = int(input())
total = 0.0

for _ in range(n):
    customer_type, amount = input().split()
    bill = CUSTOMER_TYPES[customer_type](float(amount))

    final_amount = bill.final_amount()
    print(f"{customer_type}: {final_amount:.2f}")
    total += final_amount

print(f"Total: {total:.2f}")