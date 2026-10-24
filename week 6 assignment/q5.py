class Employee:
    companyName = "Bright Horizon Technologies"
    employeeCount = 0

    def __init__(self, empName, salary):
        self.empName = empName
        self.salary = salary
        Employee.employeeCount += 1

    @staticmethod
    def printCompanyInfo():
        print(Employee.companyName)
        print(f"Employees on record: {Employee.employeeCount}")


employee1 = Employee("Divya", 65000)
employee2 = Employee("Arjun", 30000)
employee3 = Employee("Ravi", 45000)

Employee.printCompanyInfo()