class PiggyBank:
    def __init__(self, bank_id):
        self.__bank_id = bank_id
        self.__savings = 0

    @property
    def bank_id(self):
        return self.__bank_id

    def deposit(self, amount):
        if amount > 0:
            self.__savings += amount
            print("Savings =", self.__savings)

    def withdraw(self, amount):
        if amount > self.__savings:
            print("Withdrawal rejected")
        elif amount > 0:
            self.__savings -= amount
            print("Savings =", self.__savings)

    def getSavings(self):
        return self.__savings


pb = PiggyBank("PB-1")
pb.deposit(100)
pb.withdraw(30)
pb.withdraw(500)

print("Final savings =", pb.getSavings())