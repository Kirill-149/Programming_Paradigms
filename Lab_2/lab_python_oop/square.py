from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):
    """Класс квадрата (наследуется от прямоугольника)"""

    FIGURE_TYPE = "Квадрат"

    def __init__(self, side, color):
        """
        Конструктор квадрата

        Args:
            side: длина стороны
            color: цвет в виде строки
        """
        # Вызываем конструктор родительского класса (прямоугольника)
        super().__init__(side, side, color)

    @property
    def figure_type(self):
        """Возвращает тип фигуры"""
        return self.FIGURE_TYPE

    def __repr__(self):
        """Строковое представление квадрата"""
        return "{}:\nСторона: {}\nЦвет: {}\nПлощадь: {:.2f}".format(
            self.figure_type,
            self.width,  # width и height одинаковы у квадрата
            self.color.color,
            self.square()
        )
