class NameTag:
    __slots__ = ("__first_name", "__last_initial", "__locked")

    def __init__(self, full_name):
        first, last = full_name.split(" ")

        object.__setattr__(self, "_NameTag__first_name", first)
        object.__setattr__(self, "_NameTag__last_initial", last[0])
        object.__setattr__(self, "_NameTag__locked", True)

    def __setattr__(self, name, value):
        if getattr(self, "_NameTag__locked", False):
            raise AttributeError("NameTag cannot be changed")

        object.__setattr__(self, name, value)

    def getNickname(self):
        return self.__first_name + " " + self.__last_initial + "."


tag = NameTag("Maria Gomez")
print(tag.getNickname())