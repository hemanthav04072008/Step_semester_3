class PlacementRecord:
    def __init__(self, student_name, company, package_lpa):
        self.studentName = student_name
        self.company = company
        self.packageLpa = package_lpa

    def printRecord(self):
        print(
            f"{self.studentName} -> {self.company} "
            f"@ {self.packageLpa:.1f} LPA"
        )


records = [
    PlacementRecord("Ravi", "TCS", 4.5),
    PlacementRecord("Anitha", "Zoho", 6.2),
    PlacementRecord("Karthik", "Infosys", 4.0)
]

for record in records:
    record.printRecord()