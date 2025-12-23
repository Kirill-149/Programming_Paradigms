from .figure import Figure
from .color import FigureColor


class Rectangle(Figure):
    """Класс прямоугольника"""

    name = "Прямоугольник"

    def __init__(self, width: float, height: float, color: str):
        """
        Инициализирует прямоугольник

        Args:
            width: Ширина прямоугольника
            height: Высота прямоугольника
            color: Цвет прямоугольника
        """
        self.width = width
        self.height = height
        self.color_figure = FigureColor(color)

    def square(self) -> float:
        """Вычисляет площадь прямоугольника"""
        return self.width * self.height

    def __repr__(self) -> str:
        return (
            "{name}:\n"
            "  Ширина: {width}\n"
            "  Высота: {height}\n"
            "  Цвет: {color}\n"
            "  Площадь: {area:.2f}"
        ).format(
            name=self.get_name(),
            width=self.width,
            height=self.height,
            color=self.color_figure.color,
            area=self.square()
        )
