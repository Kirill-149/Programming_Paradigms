from abc import ABC, abstractmethod


class Figure(ABC):
    """Абстрактный класс геометрической фигуры"""

    @abstractmethod
    def square(self) -> float:
        """Вычисляет площадь фигуры"""
        pass

    @classmethod
    def get_name(cls) -> str:
        """Возвращает название фигуры"""
        return cls.name if hasattr(cls, 'name') else cls.__name__
