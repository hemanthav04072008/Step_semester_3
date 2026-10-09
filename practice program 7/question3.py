class NameTag:
    def __init__(self, full_name):
        first, last = full_name.split(" ")
        self.__first = first
        self.__last = last
    def getNickname(self):
        return self.__first + " " + self.__last[0] + "."
tag = NameTag("Maria Gomez")
print(tag.getNickname())