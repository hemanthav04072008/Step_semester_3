class PasswordChecker:
    __slots__ = ("__password", "__locked")

    def __init__(self, password):
        object.__setattr__(self, "_PasswordChecker__password", password)
        object.__setattr__(self, "_PasswordChecker__locked", True)

    def __setattr__(self, name, value):
        if getattr(self, "_PasswordChecker__locked", False):
            raise AttributeError("Password cannot be changed")
        object.__setattr__(self, name, value)

    def getStrength(self):
        length = len(self.__password)

        if length < 6:
            return "Weak"
        elif length <= 9:
            return "Medium"
        else:
            return "Strong"


pc1 = PasswordChecker("abcd")
pc2 = PasswordChecker("abcdefgh")
pc3 = PasswordChecker("abcdefghijkl")

print(pc1.getStrength())
print(pc2.getStrength())
print(pc3.getStrength())