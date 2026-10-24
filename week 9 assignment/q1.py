from abc import ABC, abstractmethod
import math


class Plot(ABC):
    def __init__(self, owner):
        self.owner = owner

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Plot):
    def __init__(self, owner, radius):
        super().__init__(owner)
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Plot):
    def __init__(self, owner, length, width):
        super().__init__(owner)
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


class Triangle(Plot):
    def __init__(self, owner, base, height):
        super().__init__(owner)
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


plot_types = {
    "CIRCLE": Circle,
    "RECTANGLE": Rectangle,
    "TRIANGLE": Triangle
}

n = int(input())
total_area = 0.0

for _ in range(n):
    parts = input().split()
    shape = parts[0]
    owner = parts[1]
    measurements = list(map(float, parts[2:]))

    plot = plot_types[shape](owner, *measurements)
    area = plot.calculate_area()

    print(f"{plot.owner} ({shape}): {area:.2f}")
    total_area += area

print(f"Total Area: {total_area:.2f}")