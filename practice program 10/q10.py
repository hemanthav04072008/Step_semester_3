class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        avg = sum(self.marks) / len(self.marks)

        if avg >= 75:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        elif avg >= 40:
            grade = "D"
        else:
            grade = "F"

        print(f"{self.name.upper()}: Average {avg:.1f}, Grade {grade}")


s1 = Student("Asha", [80, 90, 70])
s2 = Student("Ravi", [60, 55, 50])

s1.result()
s2.result()