class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        pass


class FullTime(Employee):
    def calculate_bonus(self):
        return self.salary * 0.10


class PartTime(Employee):
    def calculate_bonus(self):
        return self.salary * 0.05


class Intern(Employee):
    def calculate_bonus(self):
        return 2000


n = int(input())
total = 0

for i in range(n):
    employee_type, name, salary = input().split()
    salary = float(salary)

    if employee_type == "FULLTIME":
        employee = FullTime(name, salary)

    elif employee_type == "PARTTIME":
        employee = PartTime(name, salary)

    else:
        employee = Intern(name, salary)

    bonus = employee.calculate_bonus()
    total += bonus

    print(f"{employee.name}: {bonus:.2f}")

print(f"Total Bonus: {total:.2f}")