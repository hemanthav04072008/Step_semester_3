class Room:
    def __init__(self, units):
        self.units = units

    def calculate_bill(self):
        pass


class SingleRoom(Room):
    def calculate_bill(self):
        return self.units * 8


class SharedRoom(Room):
    def __init__(self, units, occupants):
        super().__init__(units)
        self.occupants = occupants

    def calculate_bill(self):
        return (self.units * 6) / self.occupants


class ACRoom(Room):
    def calculate_bill(self):
        return (self.units * 10) + 200


n = int(input())
total = 0

for i in range(n):
    data = input().split()

    room_type = data[0]
    units = int(data[1])

    if room_type == "SINGLE":
        room = SingleRoom(units)

    elif room_type == "SHARED":
        occupants = int(data[2])
        room = SharedRoom(units, occupants)

    else:
        room = ACRoom(units)

    bill = room.calculate_bill()
    total += bill

    print(f"{room_type}: {bill:.2f}")

print(f"Total: {total:.2f}")