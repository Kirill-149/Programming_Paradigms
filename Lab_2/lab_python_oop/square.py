from .rectangle import Rectangle


class Square(Rectangle):
    """Класс квадрата"""

    name = "Квадрат"

    def __init__(self, side: float, color: str):
        """
        Инициализирует квадрат

        Args:
            side: Длина стороны квадрата
            color: Цвет квадрата
        """
        super().__init__(side, side, color)

    def __repr__(self) -> str:
        return (
            f"{self.get_name()}:\n"
            f"  Сторона: {self.width}\n"
            f"  Цвет: {self.color_figure.color}\n"
            f"  Площадь: {self.square():.2f}"
        )
