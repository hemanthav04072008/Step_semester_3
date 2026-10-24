class AttendanceSheet:
    def __init__(self, max_students):
        self.__students = [None] * max_students
        self.__count = 0
        self.__max_students = max_students

    def markPresent(self, name):
        if self.isPresent(name):
            return

        if self.__count < self.__max_students:
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

print("Present count =", sheet.getPresentCount())
print("Is Ben present?", sheet.isPresent("Ben"))
print("Is Chen present?", sheet.isPresent("Chen"))