from Lab_2.figure import Figure
from Lab_2.color import Color

class Rectangle(Figure):
    FIGURE_TYPE = "Прямоугольник"

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = Color(color)

    @property
    def name(self):
        return self.FIGURE_TYPE

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return '{} {} цвета шириной {} и высотой {} площадью {}.'.format(
            self.name,
            self.color.color,
            self.width,
            self.height,
            self.area()
        )
