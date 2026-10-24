class Room:
    def __init__(self, units):
        self.units = units

    def calculate_bill(self):
        return 0.0


class SingleRoom(Room):
    def calculate_bill(self):
        return 8 * self.units


class SharedRoom(Room):
    def __init__(self, units, occupants):
        super().__init__(units)
        self.occupants = occupants

    def calculate_bill(self):
        return (6 * self.units) / self.occupants


class ACRoom(Room):
    def calculate_bill(self):
        return (10 * self.units) + 200


ROOM_TYPES = {
    "SINGLE": SingleRoom,
    "SHARED": SharedRoom,
    "AC": ACRoom
}

n = int(input())
total = 0.0

for _ in range(n):
    parts = input().split()
    room_type = parts[0]
    values = [int(value) for value in parts[1:]]

    room = ROOM_TYPES[room_type](*values)
    bill = room.calculate_bill()

    print(f"{room_type}: {bill:.2f}")
    total += bill

print(f"Total: {total:.2f}")