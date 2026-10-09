class Character:
    def __init__(self, max_health):
        self.__max_health = max_health
        self.__health = max_health

    def takeDamage(self, amount):
        self.__health = max(0, self.__health - amount)

    def heal(self, amount):
        self.__health = min(
            self.__max_health,
            self.__health + amount
        )

    def getHealth(self):
        return self.__health


c = Character(100)
c.takeDamage(30)
print(c.getHealth())

c.heal(50)
print(c.getHealth())

c.takeDamage(150)
print(c.getHealth())