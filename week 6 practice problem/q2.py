class MessWallet:
    def __init__(self, opening_balance):
        if opening_balance < 0:
            print("Warning: Negative opening balance; starting at 0.")
            self.__balance = 0.0
        else:
            self.__balance = float(opening_balance)

    def topUp(self, amount):
        if amount <= 0:
            print("Top-up rejected: amount must be positive")
        else:
            self.__balance += amount

    def deduct(self, amount):
        if amount <= 0:
            print("Deduction rejected: amount must be positive")
        elif amount > self.__balance:
            print("Deduct rejected: insufficient balance")
        else:
            self.__balance -= amount

    def getBalance(self):
        return self.__balance


wallet = MessWallet(500)
wallet.topUp(200)
print(f"Balance after top-up: {wallet.getBalance():.1f}")

wallet.deduct(1000)
print(f"Final balance: {wallet.getBalance():.1f}")