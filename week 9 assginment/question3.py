from abc import ABC, abstractmethod

class Student(ABC):
    TRANSPORT_FEE = 12000

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_fee(self):
        pass

class DayScholar(Student):
    def calculate_fee(self):
        return 40000 + self.TRANSPORT_FEE

class Hosteller(Student):
    def calculate_fee(self):
        return 40000 + 60000

class Scholar(Student):
    def calculate_fee(self):
        return 20000 + self.TRANSPORT_FEE

n = int(input())
total = 0

for _ in range(n):
    student_type, name = input().split()

    if student_type == "DAY_SCHOLAR":
        student = DayScholar(name)
    elif student_type == "HOSTELLER":
        student = Hosteller(name)
    else:
        student = Scholar(name)

    fee = student.calculate_fee()
    print(f"{student.name}: {fee:.2f}")
    total += fee

print(f"Total Collected: {total:.2f}")