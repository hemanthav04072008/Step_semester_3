class PiggyBank:
    def __init__(self, bankid):
        self.id = bankid
        self.savings = 0
    def deposit(self, amount):
        self.savings += amount
    def withdraw(self, amount):
        if amount <= self.savings:
            self.savings -= amount
    def getSavings(self):
        return self.savings
pb =PiggyBank("PB-1")
pb.deposit(100)
print(pb.getSavings())
pb.withdraw(30)
print(pb.getSavings())
pb.withdraw(500)
print(pb.getSavings())