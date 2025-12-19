import math
from lab_python_oop.figure import Figure
from lab_python_oop.color import Color

class Circle(Figure):
    """Класс круга"""

    FIGURE_TYPE = "Круг"

    def __init__(self, radius, color):
        """
        Конструктор круга

        Args:
            radius: радиус
            color: цвет в виде строки
        """
        self.radius = radius
        self.color = Color(color)

    @property
    def figure_type(self):
        """Возвращает тип фигуры"""
        return self.FIGURE_TYPE

    def square(self):
        """Вычисление площади круга с использованием math.pi"""
        return math.pi * self.radius ** 2

    def __repr__(self):
        """Строковое представление круга"""
        return "{}:\nРадиус: {}\nЦвет: {}\nПлощадь: {:.2f}".format(
            self.figure_type,
            self.radius,
            self.color.color,
            self.square()
        )
