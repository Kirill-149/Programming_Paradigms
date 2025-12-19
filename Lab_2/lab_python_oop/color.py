class Color:
    """Класс для хранения цвета фигуры"""

    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        """Свойство для получения цвета"""
        return self._color

    @color.setter
    def color(self, value):
        """Свойство для установки цвета"""
        self._color = value

    def __repr__(self):
        return self._color
