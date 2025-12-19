"""
Основной файл для тестирования классов геометрических фигур
"""

from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

# Импортируем внешний пакет (colorama для цветного вывода в консоль)
from colorama import init, Fore, Back, Style

def main():
    """Основная функция тестирования"""

    # Инициализируем colorama для работы с цветным выводом
    init(autoreset=True)

    # N = 5 (для примера, можно заменить на свой номер варианта)
    N = 5

    print(Fore.CYAN + "=" * 50)
    print(Fore.YELLOW + "ТЕСТИРОВАНИЕ КЛАССОВ ГЕОМЕТРИЧЕСКИХ ФИГУР")
    print(Fore.CYAN + "=" * 50)

    # Создание объектов
    print(Fore.GREEN + "\n1. Создание объектов:")

    # Прямоугольник синего цвета шириной N и высотой N
    rectangle = Rectangle(N, N, "синий")

    # Круг зеленого цвета радиусом N
    circle = Circle(N, "зеленый")

    # Квадрат красного цвета со стороной N
    square = Square(N, "красный")

    # Вывод информации о фигурах с использованием colorama
    print(Fore.MAGENTA + "\n2. Информация о фигурах:")
    print(Fore.WHITE + "-" * 50)

    print(Fore.BLUE + str(rectangle))
    print(Fore.WHITE + "-" * 50)

    print(Fore.GREEN + str(circle))
    print(Fore.WHITE + "-" * 50)

    print(Fore.RED + str(square))
    print(Fore.WHITE + "-" * 50)

    # Демонстрация работы с абстрактными методами
    print(Fore.YELLOW + "\n3. Демонстрация абстрактных методов:")
    figures = [rectangle, circle, square]

    for i, figure in enumerate(figures, 1):
        print(Fore.CYAN + f"Фигура {i}: {figure.figure_type}")
        print(f"Площадь: {figure.square():.2f}")
        print(f"Цвет: {figure.color.color}")
        print()

    # Демонстрация использования внешнего пакета colorama
    print(Fore.YELLOW + "\n4. Демонстрация внешнего пакета (colorama):")
    print(Fore.RED + "Красный текст" + Fore.RESET)
    print(Fore.GREEN + "Зеленый текст" + Fore.RESET)
    print(Fore.BLUE + "Синий текст" + Fore.RESET)
    print(Back.YELLOW + Fore.BLACK + "Желтый фон с черным текстом" + Style.RESET_ALL)
    print(Fore.BLACK + Back.WHITE + "Белый фон с черным текстом" + Style.RESET_ALL)

    # Дополнительные возможности colorama
    print(Fore.YELLOW + "\n5. Дополнительные стили colorama:")
    print(Style.BRIGHT + "Жирный текст" + Style.NORMAL)
    print(Style.DIM + "Тусклый текст" + Style.NORMAL)

    # Проверка типов фигур через свойство класса
    print(Fore.YELLOW + "\n6. Типы фигур через свойства класса:")
    print(f"Тип прямоугольника: {rectangle.figure_type}")
    print(f"Тип круга: {circle.figure_type}")
    print(f"Тип квадрата: {square.figure_type}")

    # Тестирование свойства цвета
    print(Fore.YELLOW + "\n7. Тестирование свойства цвета:")
    print(f"Цвет прямоугольника: {rectangle.color.color}")

    # Изменение цвета через свойство
    rectangle.color.color = "фиолетовый"
    print(f"Новый цвет прямоугольника: {rectangle.color.color}")

    print(Fore.CYAN + "\n" + "=" * 50)
    print(Fore.YELLOW + "ТЕСТИРОВАНИЕ ЗАВЕРШЕНО")
    print(Fore.CYAN + "=" * 50)

if __name__ == "__main__":
    main()
