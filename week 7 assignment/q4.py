class TrafficLight:
    def __init__(self, light_id):
        self.__light_id = light_id
        self.__colors = ("RED", "GREEN", "YELLOW")
        self.__index = 0

    @property
    def light_id(self):
        return self.__light_id

    def getColor(self):
        return self.__colors[self.__index]

    def next(self):
        self.__index = (self.__index + 1) % len(self.__colors)
        return self.getColor()


t = TrafficLight("TL-9")

print(t.getColor())
print(t.next())
print(t.next())
print(t.next())
print(t.next())