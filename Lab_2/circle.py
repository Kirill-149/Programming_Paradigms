from Lab_2.figure import Figure
from Lab_2.color import Color
import math

class Circle(Figure):
    FIGURE_TYPE = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.color = Color(color)

    @property
    def name(self):
        return self.FIGURE_TYPE

    def area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {:.2f}.'.format(
            self.name,
            self.color.color,
            self.radius,
            self.area()
        )
