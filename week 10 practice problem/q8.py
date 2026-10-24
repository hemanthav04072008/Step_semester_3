import sys

marks_list = list(map(int, sys.stdin.read().split()))

for marks in marks_list:
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "F"

    print("Grade", grade)