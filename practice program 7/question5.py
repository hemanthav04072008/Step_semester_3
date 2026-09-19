class AttendanceSheet:
    def __init__(self, size):
        self.__students = [None] * size
        self.__count = 0
    def markPresent(self, name):
        if self.isPresent(name):
            return
        if self.__count < len(self.__students):
            self.__students[self.__count] = name
            self.__count += 1
    def getPresentCount(self):
        return self.__count
    def isPresent(self, name):
        for i in range(self.__count):
            if self.__students[i] == name:
                return True
        return False
sheet = AttendanceSheet(30)
sheet.markPresent("Ana")
sheet.markPresent("Ben")
sheet.markPresent("Ana")
print(sheet.getPresentCount())
print(sheet.isPresent("Ben"))
print(sheet.isPresent("Chen"))