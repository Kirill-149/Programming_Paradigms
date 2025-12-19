from lab_python_oop.figure import Figure
from lab_python_oop.color import Color

class Rectangle(Figure):
    """Класс прямоугольника"""

    FIGURE_TYPE = "Прямоугольник"

    def __init__(self, width, height, color):
        """
        Конструктор прямоугольника

        Args:
            width: ширина
            height: высота
            color: цвет в виде строки
        """
        self.width = width
        self.height = height
        self.color = Color(color)

    @property
    def figure_type(self):
        """Возвращает тип фигуры"""
        return self.FIGURE_TYPE

    def square(self):
        """Вычисление площади прямоугольника"""
        return self.width * self.height

    def __repr__(self):
        """Строковое представление прямоугольника"""
        return "{}:\nШирина: {}\nВысота: {}\nЦвет: {}\nПлощадь: {:.2f}".format(
            self.figure_type,
            self.width,
            self.height,
            self.color.color,
            self.square()
        )
