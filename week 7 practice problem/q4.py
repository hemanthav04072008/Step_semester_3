class Locker:
    def __init__(self, locker_number, code):
        self.__locker_number = locker_number
        self.__code = code

    @property
    def locker_number(self):
        return self.__locker_number

    def changeCode(self, current_code, new_code):
        if current_code == self.__code:
            self.__code = new_code
            print("Code changed successfully")
        else:
            print("Change rejected")


locker = Locker(101, "1234")

locker.changeCode("1234", "5678")
locker.changeCode("0000", "9999")

print("Locker number =", locker.locker_number)