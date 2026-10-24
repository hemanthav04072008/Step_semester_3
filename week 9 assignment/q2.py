from abc import ABC, abstractmethod


class Staff(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_pay(self):
        pass


class FullTimeStaff(Staff):
    def __init__(self, name, weekly_salary):
        super().__init__(name)
        self.weekly_salary = weekly_salary

    def calculate_pay(self):
        return self.weekly_salary


class HourlyStaff(Staff):
    def __init__(self, name, hours, rate):
        super().__init__(name)
        self.hours = hours
        self.rate = rate

    def calculate_pay(self):
        regular_hours = min(self.hours, 40)
        overtime_hours = max(self.hours - 40, 0)

        return (
            regular_hours * self.rate
            + overtime_hours * self.rate * 1.5
        )


class Intern(Staff):
    def __init__(self, name, stipend):
        super().__init__(name)
        self.stipend = stipend

    def calculate_pay(self):
        return self.stipend


staff_types = {
    "FULLTIME": FullTimeStaff,
    "HOURLY": HourlyStaff,
    "INTERN": Intern
}

n = int(input())
total_payroll = 0.0

for _ in range(n):
    parts = input().split()
    staff_type = parts[0]
    name = parts[1]
    values = list(map(float, parts[2:]))

    staff = staff_types[staff_type](name, *values)
    pay = staff.calculate_pay()

    print(f"{staff.name}: {pay:.2f}")
    total_payroll += pay

print(f"Total Payroll: {total_payroll:.2f}")