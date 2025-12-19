from abc import ABC, abstractmethod

class Figure(ABC):
    """Абстрактный класс геометрической фигуры"""

    @property
    @abstractmethod
    def figure_type(self):
        """Тип фигуры (должен быть реализован в дочерних классах)"""
        pass

    @abstractmethod
    def square(self):
        """Абстрактный метод вычисления площади (должен быть реализован в дочерних классах)"""
        pass

    def __repr__(self):
        """Строковое представление фигуры с цветом и площадью"""
        return "Тип фигуры: {}\nЦвет: {}\nПлощадь: {:.2f}".format(
            self.figure_type,
            self.color.color,
            self.square()
        )
