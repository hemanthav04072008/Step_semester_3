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


class BankTransferPayment(Payment):
    def calculate_amount(self):
        return self.amount


n = int(input())
total = 0

for i in range(n):
    payment_type, amount = input().split()
    amount = float(amount)

    if payment_type == "CARD":
        payment = CardPayment(amount)
    elif payment_type == "WALLET":
        payment = WalletPayment(amount)
    else:
        payment = BankTransferPayment(amount)

    result = payment.calculate_amount()
    total += result

    print(f"{payment_type}: {result:.2f}")

print(f"Total: {total:.2f}")