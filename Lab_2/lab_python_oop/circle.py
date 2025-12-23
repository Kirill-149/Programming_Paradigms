import math
from .figure import Figure
from .color import FigureColor


class Circle(Figure):
    """Класс круга"""

    name = "Круг"

    def __init__(self, radius: float, color: str):
        """
        Инициализирует круг

        Args:
            radius: Радиус круга
            color: Цвет круга
        """
        self.radius = radius
        self.color_figure = FigureColor(color)

    def square(self) -> float:
        """Вычисляет площадь круга"""
        return math.pi * (self.radius ** 2)

    def __repr__(self) -> str:
        return (
            f"{self.get_name()}:\n"
            f"  Радиус: {self.radius}\n"
            f"  Цвет: {self.color_figure.color}\n"
            f"  Площадь: {self.square():.2f}"
        )
