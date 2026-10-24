class Payment:
    def __init__(self, amount):
        self.amount = amount

    def calculate_amount(self):
        return self.amount


class CardPayment(Payment):
    def calculate_amount(self):
        return self.amount * 1.02


class WalletPayment(Payment):
    def calculate_amount(self):
        return self.amount * 1.01


class BankTransfer(Payment):
    def calculate_amount(self):
        return self.amount


PAYMENT_TYPES = {
    "CARD": CardPayment,
    "WALLET": WalletPayment,
    "BANKTRANSFER": BankTransfer
}

n = int(input())
payments = []

for _ in range(n):
    payment_type, amount = input().split()
    payment = PAYMENT_TYPES[payment_type](float(amount))
    payments.append((payment_type, payment))

total = 0

for payment_type, payment in payments:
    adjusted = payment.calculate_amount()
    print(f"{payment_type}: {adjusted:.2f}")
    total += adjusted

print(f"Total: {total:.2f}")