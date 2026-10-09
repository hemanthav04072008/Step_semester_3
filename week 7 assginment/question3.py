class PasswordChecker:
    def __init__(self, password):
        self.__password = password

    def getStrength(self):
        length = len(self.__password)

        if length < 6:
            return "Weak"
        elif length <= 9:
            return "Medium"
        else:
            return "Strong"


pc = PasswordChecker("abcd")
print(pc.getStrength())

pc2 = PasswordChecker("abcdefghij")
print(pc2.getStrength())