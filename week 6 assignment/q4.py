class HallTicket:
    def __init__(self, studentName, seatNumber):
        self.studentName = studentName
        self.seatNumber = seatNumber


priya = HallTicket("Priya", 0)
copy = priya

copy.seatNumber = 45

print(f"Priya's seatNumber (via first variable): {priya.seatNumber}")
print(f"copy == priya: {copy is priya}")

separate = HallTicket("Priya", 45)
print(f"separate == priya: {separate is priya}")