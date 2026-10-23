day = int(input("Enter day number (1-7): "))

days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

if day in days:
    print(days[day])
else:
    print("Invalid day number")