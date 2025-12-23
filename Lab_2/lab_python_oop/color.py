class FigureColor:
    """Класс для описания цвета геометрической фигуры"""

    def __init__(self, color: str):
        """
        Инициализирует цвет фигуры

        Args:
            color: Название цвета
        """
        self._color = color

    @property
    def color(self) -> str:
        """Возвращает цвет фигуры"""
        return self._color

    @color.setter
    def color(self, value: str):
        """Устанавливает цвет фигуры"""
        self._color = value

    def __repr__(self) -> str:
        return f"FigureColor('{self._color}')"
