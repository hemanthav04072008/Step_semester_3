from abc import ABC, abstractmethod

class Staff(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_pay(self):
        pass

class FullTime(Staff):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def calculate_pay(self):
        return self.salary

class Hourly(Staff):
    def __init__(self, name, hours, rate):
        super().__init__(name)
        self.hours = hours
        self.rate = rate

    def calculate_pay(self):
        if self.hours <= 40:
            return self.hours * self.rate
        return 40 * self.rate + (self.hours - 40) * self.rate * 1.5

class Intern(Staff):
    def __init__(self, name, stipend):
        super().__init__(name)
        self.stipend = stipend

    def calculate_pay(self):
        return self.stipend

n = int(input())
staff_list = []

for _ in range(n):
    data = input().split()
    staff_type = data[0]

    if staff_type == "FULLTIME":
        staff_list.append(FullTime(data[1], float(data[2])))
    elif staff_type == "HOURLY":
        staff_list.append(Hourly(data[1], float(data[2]), float(data[3])))
    elif staff_type == "INTERN":
        staff_list.append(Intern(data[1], float(data[2])))

total = 0

for staff in staff_list:
    pay = staff.calculate_pay()
    print(f"{staff.name}: {pay:.2f}")
    total += pay

print(f"Total Payroll: {total:.2f}")