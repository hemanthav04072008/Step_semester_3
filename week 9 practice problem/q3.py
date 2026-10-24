class Student:
    TRANSPORT_FEE = 12000

    def __init__(self, name, tuition):
        self.name = name
        self.tuition = tuition

    def uses_bus(self):
        return False

    def additional_fee(self):
        return 0

    def calculate_total_fee(self):
        total = self.tuition + self.additional_fee()

        if self.uses_bus():
            total += Student.TRANSPORT_FEE

        return total


class DayScholar(Student):
    def __init__(self, name):
        super().__init__(name, 40000)

    def uses_bus(self):
        return True


class Hosteller(Student):
    def __init__(self, name):
        super().__init__(name, 40000)

    def additional_fee(self):
        return 60000


class ScholarshipStudent(Student):
    def __init__(self, name):
        super().__init__(name, 20000)

    def uses_bus(self):
        return True


student_types = {
    "DAY_SCHOLAR": DayScholar,
    "HOSTELLER": Hosteller,
    "SCHOLAR": ScholarshipStudent
}

n = int(input())
total_collected = 0.0

for _ in range(n):
    student_type, name = input().split()
    student = student_types[student_type](name)

    fee = student.calculate_total_fee()
    print(f"{student.name}: {fee:.2f}")
    total_collected += fee

print(f"Total Collected: {total_collected:.2f}")