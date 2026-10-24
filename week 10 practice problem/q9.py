import sys

years = list(map(int, sys.stdin.read().split()))

for year in years:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("Leap year")
    else:
        print("Not a leap year")