class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return 0.0


class FullTimeEmployee(Employee):
    def calculate_bonus(self):
        return self.salary * 0.10


class PartTimeEmployee(Employee):
    def calculate_bonus(self):
        return self.salary * 0.05


class Intern(Employee):
    def calculate_bonus(self):
        return 2000.0


EMPLOYEE_TYPES = {
    "FULLTIME": FullTimeEmployee,
    "PARTTIME": PartTimeEmployee,
    "INTERN": Intern
}

n = int(input())
total_bonus = 0.0

for _ in range(n):
    employee_type, name, salary = input().split()
    employee = EMPLOYEE_TYPES[employee_type](name, float(salary))

    bonus = employee.calculate_bonus()
    print(f"{employee.name}: {bonus:.2f}")
    total_bonus += bonus

print(f"Total Bonus: {total_bonus:.2f}")