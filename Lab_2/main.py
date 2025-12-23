#!/usr/bin/env python3
"""
Основной файл для тестирования классов геометрических фигур
"""

from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

# Для демонстрации использования внешнего пакета
try:
    from colorama import init, Fore, Back, Style
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False
    print("Пакет colorama не установлен. Для цветного вывода установите его: pip install colorama")


def main():
    """Основная функция тестирования"""

    # Установим N = 17 (номер варианта)
    N = 17

    print("=" * 50)
    print("Тестирование классов геометрических фигур")
    print("=" * 50)
    print(f"Используемое значение N = {N}")
    print()

    # 1. Создаем прямоугольник синего цвета шириной N и высотой N
    print("1. Создание прямоугольника:")
    rect = Rectangle(width=N, height=N, color="синий")
    print(rect)
    print()

    # 2. Создаем круг зеленого цвета радиусом N
    print("2. Создание круга:")
    circle = Circle(radius=N, color="зеленый")
    print(circle)
    print()

    # 3. Создаем квадрат красного цвета со стороной N
    print("3. Создание квадрата:")
    square = Square(side=N, color="красный")
    print(square)
    print()

    # 4. Демонстрация работы с абстрактным классом
    print("4. Проверка полиморфизма:")
    figures = [rect, circle, square]

    for i, figure in enumerate(figures, 1):
        print(f"Фигура {i}: {figure.get_name()}")
        print(f"  Площадь: {figure.square():.2f}")
        print(f"  Представление:\n{repr(figure)}")
        print()

    # 5. Вызов метода из внешнего пакета (colorama)
    print("5. Использование внешнего пакета colorama:")
    if COLORAMA_AVAILABLE:
        # Инициализация colorama
        init(autoreset=True)

        # Использование colorama для цветного вывода
        print(Fore.GREEN + "Этот текст выведен зеленым цветом с помощью colorama!")
        print(Back.YELLOW + Fore.BLACK + "А этот текст на желтом фоне")
        print(Style.BRIGHT + Fore.BLUE + "И этот текст синий и жирный")

        # Создадим цветные версии наших фигур
        print("\nЦветное представление фигур:")
        color_figures = [
            (Fore.BLUE, "Прямоугольник", f"синий, размер: {N}x{N}, площадь: {rect.square():.2f}"),
            (Fore.GREEN, "Круг", f"зеленый, радиус: {N}, площадь: {circle.square():.2f}"),
            (Fore.RED, "Квадрат", f"красный, сторона: {N}, площадь: {square.square():.2f}"),
        ]

        for color, name, description in color_figures:
            print(color + f"{name}: {description}")
    else:
        print("Для цветного вывода установите пакет colorama: pip install colorama")
        print("Пример использования:")
        print("  from colorama import Fore, Back, Style, init")
        print("  init()  # Инициализация")
        print("  print(Fore.RED + 'Красный текст')")

    print("\n" + "=" * 50)
    print("Тестирование завершено!")
    print("=" * 50)


if __name__ == "__main__":
    main()
