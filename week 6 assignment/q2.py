class PayrollAccount:
    def __init__(self, basicSalary):
        if basicSalary < 0:
            print("Warning: Negative salary. Starting at 0.")
            self.__basicSalary = 0.0
        else:
            self.__basicSalary = float(basicSalary)

        self.__bonus = 0.0

    def creditBonus(self, amount):
        if amount <= 0:
            print("Bonus rejected: amount must be positive")
        else:
            self.__bonus += amount
            print(f"Bonus credited: Rs {amount:.1f}")

    def deductTax(self, percent):
        if percent < 0 or percent > 100:
            print("Tax deduction rejected: invalid percentage")
        else:
            self.__basicSalary -= self.__basicSalary * percent / 100
            print(f"Tax deducted: {percent}%")

    def getNetSalary(self):
        return self.__basicSalary + self.__bonus


account = PayrollAccount(50000)
account.creditBonus(5000)
account.deductTax(10)

print(f"Net salary: Rs {account.getNetSalary():.1f}")