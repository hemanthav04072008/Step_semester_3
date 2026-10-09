from abc import ABC, abstractmethod
import math

class Plot(ABC):
    def __init__(self, owner):
        self.owner = owner

    @abstractmethod
    def area(self):
        pass

class Circle(Plot):
    def __init__(self, owner, radius):
        super().__init__(owner)
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

class Rectangle(Plot):
    def __init__(self, owner, length, width):
        super().__init__(owner)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Plot):
    def __init__(self, owner, base, height):
        super().__init__(owner)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

n = int(input())
plots = []

for _ in range(n):
    data = input().split()
    shape = data[0]
    owner = data[1]

    if shape == "CIRCLE":
        plots.append(Circle(owner, float(data[2])))
    elif shape == "RECTANGLE":
        plots.append(Rectangle(owner, float(data[2]), float(data[3])))
    elif shape == "TRIANGLE":
        plots.append(Triangle(owner, float(data[2]), float(data[3])))

total = 0

for plot in plots:
    a = plot.area()
    print(f"{plot.owner} ({plot.__class__.__name__.upper()}): {a:.2f}")
    total += a

print(f"Total Area: {total:.2f}")