class TrafficLight:
    def __init__(self, light_id):
        self.__id = light_id
        self.__colors = ["RED", "GREEN", "YELLOW"]
        self.__index = 0
        self.__color = self.__colors[self.__index]

    def next(self):
        self.__index = (self.__index + 1) % len(self.__colors)
        self.__color = self.__colors[self.__index]

    def getColor(self):
        return self.__color

    def getId(self):
        return self.__id


t = TrafficLight("TL-9")
print(t.getColor())

t.next()
print(t.getColor())

t.next()
print(t.getColor())

t.next()
print(t.getColor())