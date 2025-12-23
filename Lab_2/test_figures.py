#!/usr/bin/env python3
"""
Модульные тесты для геометрических фигур
"""

import unittest
import math
from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


class TestFigureColor(unittest.TestCase):
    """Тесты для класса FigureColor"""

    def test_color_initialization(self):
        """Тест инициализации цвета"""
        color = FigureColor("красный")
        self.assertEqual(color.color, "красный")

    def test_color_setter(self):
        """Тест изменения цвета"""
        color = FigureColor("синий")
        color.color = "зеленый"
        self.assertEqual(color.color, "зеленый")

    def test_repr_method(self):
        """Тест строкового представления"""
        color = FigureColor("красный")
        self.assertIn("красный", repr(color))
        self.assertIn("FigureColor", repr(color))


class TestRectangle(unittest.TestCase):
    """Тесты для класса Rectangle"""

    def setUp(self):
        """Настройка тестовых данных"""
        self.rectangle = Rectangle(5, 10, "синий")

    def test_rectangle_initialization(self):
        """Тест инициализации прямоугольника"""
        self.assertEqual(self.rectangle.width, 5)
        self.assertEqual(self.rectangle.height, 10)
        self.assertEqual(self.rectangle.color_figure.color, "синий")

    def test_rectangle_square(self):
        """Тест вычисления площади прямоугольника"""
        self.assertEqual(self.rectangle.square(), 50)

        # Проверка с другими значениями
        rect2 = Rectangle(3, 7, "красный")
        self.assertEqual(rect2.square(), 21)

    def test_rectangle_name(self):
        """Тест получения названия фигуры"""
        self.assertEqual(self.rectangle.get_name(), "Прямоугольник")
        self.assertEqual(Rectangle.name, "Прямоугольник")

    def test_rectangle_repr(self):
        """Тест строкового представления прямоугольника"""
        repr_str = repr(self.rectangle)
        self.assertIn("Прямоугольник", repr_str)
        self.assertIn("Ширина: 5", repr_str)
        self.assertIn("Высота: 10", repr_str)
        self.assertIn("Цвет: синий", repr_str)
        self.assertIn("Площадь: 50.00", repr_str)

    def test_rectangle_with_float_values(self):
        """Тест прямоугольника с дробными значениями"""
        rect = Rectangle(3.5, 4.2, "зеленый")
        self.assertAlmostEqual(rect.square(), 14.7, places=5)


class TestCircle(unittest.TestCase):
    """Тесты для класса Circle"""

    def setUp(self):
        """Настройка тестовых данных"""
        self.circle = Circle(5, "красный")

    def test_circle_initialization(self):
        """Тест инициализации круга"""
        self.assertEqual(self.circle.radius, 5)
        self.assertEqual(self.circle.color_figure.color, "красный")

    def test_circle_square(self):
        """Тест вычисления площади круга"""
        expected_area = math.pi * 25  # π * r²
        self.assertAlmostEqual(self.circle.square(), expected_area, places=5)

        # Проверка с другими значениями
        circle2 = Circle(10, "синий")
        expected_area2 = math.pi * 100
        self.assertAlmostEqual(circle2.square(), expected_area2, places=5)

    def test_circle_name(self):
        """Тест получения названия фигуры"""
        self.assertEqual(self.circle.get_name(), "Круг")
        self.assertEqual(Circle.name, "Круг")

    def test_circle_repr(self):
        """Тест строкового представления круга"""
        repr_str = repr(self.circle)
        self.assertIn("Круг", repr_str)
        self.assertIn("Радиус: 5", repr_str)
        self.assertIn("Цвет: красный", repr_str)

        # Проверяем, что площадь округлена до 2 знаков
        area_str = f"{math.pi * 25:.2f}"
        self.assertIn(f"Площадь: {area_str}", repr_str)


class TestSquare(unittest.TestCase):
    """Тесты для класса Square"""

    def setUp(self):
        """Настройка тестовых данных"""
        self.square = Square(7, "зеленый")

    def test_square_initialization(self):
        """Тест инициализации квадрата"""
        self.assertEqual(self.square.width, 7)
        self.assertEqual(self.square.height, 7)  # У квадрата высота = ширина
        self.assertEqual(self.square.color_figure.color, "зеленый")

    def test_square_inheritance(self):
        """Тест наследования квадрата от прямоугольника"""
        self.assertIsInstance(self.square, Rectangle)
        self.assertIsInstance(self.square, Figure)

    def test_square_square(self):
        """Тест вычисления площади квадрата"""
        self.assertEqual(self.square.square(), 49)

        # Проверка с другими значениями
        square2 = Square(10, "синий")
        self.assertEqual(square2.square(), 100)

    def test_square_name(self):
        """Тест получения названия фигуры"""
        self.assertEqual(self.square.get_name(), "Квадрат")
        self.assertEqual(Square.name, "Квадрат")

    def test_square_repr(self):
        """Тест строкового представления квадрата"""
        repr_str = repr(self.square)
        self.assertIn("Квадрат", repr_str)
        self.assertIn("Сторона: 7", repr_str)
        self.assertIn("Цвет: зеленый", repr_str)
        self.assertIn("Площадь: 49.00", repr_str)


class TestAbstractClass(unittest.TestCase):
    """Тесты для абстрактного класса Figure"""

    def test_cannot_instantiate_abstract_class(self):
        """Тест, что нельзя создать экземпляр абстрактного класса"""
        with self.assertRaises(TypeError):
            Figure()  # Должно вызвать TypeError

    def test_all_figures_implement_square_method(self):
        """Тест, что все фигуры реализуют метод square"""
        # Проверяем, что у всех классов есть метод square
        for cls in [Rectangle, Circle, Square]:
            self.assertTrue(hasattr(cls, 'square'))
            self.assertTrue(callable(getattr(cls, 'square')))

    def test_all_figures_have_name_attribute(self):
        """Тест, что все фигуры имеют атрибут name"""
        for cls in [Rectangle, Circle, Square]:
            self.assertTrue(hasattr(cls, 'name'))
            self.assertIsInstance(cls.name, str)


class TestFigurePolymorphism(unittest.TestCase):
    """Тесты полиморфизма фигур"""

    def setUp(self):
        """Настройка тестовых данных"""
        self.figures = [
            Rectangle(3, 4, "красный"),
            Circle(5, "синий"),
            Square(6, "зеленый")
        ]

    def test_polymorphic_square_method(self):
        """Тест полиморфного вызова метода square"""
        expected_areas = [12, math.pi * 25, 36]

        for figure, expected_area in zip(self.figures, expected_areas):
            if isinstance(figure, Circle):
                self.assertAlmostEqual(figure.square(), expected_area, places=5)
            else:
                self.assertEqual(figure.square(), expected_area)

    def test_polymorphic_get_name_method(self):
        """Тест полиморфного вызова метода get_name"""
        expected_names = ["Прямоугольник", "Круг", "Квадрат"]

        for figure, expected_name in zip(self.figures, expected_names):
            self.assertEqual(figure.get_name(), expected_name)

    def test_all_figures_are_figure_instances(self):
        """Тест, что все фигуры являются экземплярами Figure"""
        for figure in self.figures:
            self.assertIsInstance(figure, Figure)


class TestEdgeCases(unittest.TestCase):
    """Тесты граничных случаев"""

    def test_rectangle_with_zero_dimensions(self):
        """Тест прямоугольника с нулевыми размерами"""
        rect = Rectangle(0, 10, "красный")
        self.assertEqual(rect.square(), 0)

        rect2 = Rectangle(10, 0, "синий")
        self.assertEqual(rect2.square(), 0)

    def test_circle_with_zero_radius(self):
        """Тест круга с нулевым радиусом"""
        circle = Circle(0, "зеленый")
        self.assertEqual(circle.square(), 0)

    def test_square_with_zero_side(self):
        """Тест квадрата с нулевой стороной"""
        square = Square(0, "желтый")
        self.assertEqual(square.square(), 0)

    def test_negative_values(self):
        """Тест с отрицательными значениями (должны работать для площади)"""
        rect = Rectangle(-5, 10, "красный")
        self.assertEqual(rect.square(), -50)  # Отрицательная площадь логически возможна

        circle = Circle(-5, "синий")
        self.assertEqual(circle.square(), math.pi * 25)  # Квадрат радиуса всегда положителен


if __name__ == '__main__':
    # Запуск тестов с подробным выводом
    print("=" * 60)
    print("Запуск модульных тестов для геометрических фигур")
    print("=" * 60)
    print()

    # Создаем тестовый набор
    loader = unittest.TestLoader()

    # Добавляем все тестовые классы
    test_classes = [
        TestFigureColor,
        TestRectangle,
        TestCircle,
        TestSquare,
        TestAbstractClass,
        TestFigurePolymorphism,
        TestEdgeCases
    ]

    # Создаем тестовый набор
    test_suite = unittest.TestSuite()
    for test_class in test_classes:
        tests = loader.loadTestsFromTestCase(test_class)
        test_suite.addTests(tests)

    # Запускаем тесты
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)

    # Выводим итоговую статистику
    print("\n" + "=" * 60)
    print(f"Всего тестов: {result.testsRun}")
    print(f"Пройдено успешно: {result.testsRun - len(result.failures) - len(result.errors)}")

    if result.failures:
        print(f"Провалено тестов: {len(result.failures)}")
        for test, traceback in result.failures:
            print(f"\nПровален тест: {test}")
            print(traceback)

    if result.errors:
        print(f"Ошибок в тестах: {len(result.errors)}")
        for test, traceback in result.errors:
            print(f"\nОшибка в тесте: {test}")
            print(traceback)

    if result.wasSuccessful():
        print("\n✓ Все тесты успешно пройдены!")
    else:
        print("\n✗ Некоторые тесты не прошли")
    print("=" * 60)
