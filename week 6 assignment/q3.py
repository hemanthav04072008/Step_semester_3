class Employee:
    def __init__(self, empId, empName, salary=None):
        self.empId = empId
        self.empName = empName

        if salary is None:
            self.salary = 0.0
            self.isIntern = True
        else:
            self.salary = salary
            self.isIntern = False

    def printProfile(self):
        print(
            f"{self.empId} | {self.empName} | "
            f"Rs {self.salary:.1f} | Intern: {str(self.isIntern).lower()}"
        )


permanent = Employee("E-101", "Divya", 65000)
intern = Employee("E-102", "Arjun")

permanent.printProfile()
intern.printProfile()