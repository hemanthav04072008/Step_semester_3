import ast
import sys

for line in sys.stdin.read().splitlines():
    if not line.strip():
        continue

    name, marks_part = line.split("[", 1)
    name = name.strip()
    marks = ast.literal_eval("[" + marks_part)

    average = sum(marks) / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    print(f"{name.upper()}: Average {average:.1f}, Grade {grade}")