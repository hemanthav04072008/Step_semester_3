class Course:
    def __init__(self, code, title, credits, labCredits=0):
        self.code = code
        self.title = title
        self.credits = credits
        self.labCredits = labCredits

    def totalCredits(self):
        return self.credits + self.labCredits


theory_course = Course("21CSC201J", "Data Structures", 4)
lab_course = Course("21CSC205L", "DSA Lab", 3, 1)

print(f"{theory_course.code} total credits: {theory_course.totalCredits()}")
print(f"{lab_course.code} total credits: {lab_course.totalCredits()}")