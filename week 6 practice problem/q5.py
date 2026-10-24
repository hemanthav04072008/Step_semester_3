class Student:
    collegeName = "SRM Institute of Science and Technology"
    studentCount = 0

    def __init__(self, name, attendance):
        self.name = name
        self.attendance = attendance
        Student.studentCount += 1

    @staticmethod
    def printCollegeInfo():
        print(Student.collegeName)
        print(f"Students created: {Student.studentCount}")


student1 = Student("Ravi", 90)
student2 = Student("Anitha", 95)

Student.printCollegeInfo()