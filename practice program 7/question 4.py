class Locker:
    def __init__(self, number, code):
        self.__number = number
        self.__code = code
    def changeCode(self, old_code, new_code):
        if old_code == self.__code:
            self.__code = new_code
            print("Success")
        else:
            print("Rejected")
l = Locker(101, "1234")
l.changeCode("1234", "5678")
l.changeCode("0000", "9999")