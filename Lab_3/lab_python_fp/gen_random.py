# lab_python_fp/gen_random.py
import random

def gen_random(num_count, begin, end):
    """
    Генератор случайных чисел в заданном диапазоне.

    Args:
        num_count: Количество случайных чисел для генерации
        begin: Нижняя граница диапазона (включительно)
        end: Верхняя граница диапазона (включительно)

    Yields:
        Случайное целое число в диапазоне [begin, end]
    """
    for _ in range(num_count):
        yield random.randint(begin, end)


def test_gen_random():
    """Тестирование генератора случайных чисел"""
    print("Тестирование генератора gen_random...")

    print("\n1. Тест: 5 чисел в диапазоне от 1 до 3:")
    print("   gen_random(5, 1, 3) ->")
    result = list(gen_random(5, 1, 3))
    print(f"     {result}")

    print("\n2. Тест: 10 чисел в диапазоне от 0 до 10:")
    print("   gen_random(10, 0, 10) ->")
    result = list(gen_random(10, 0, 10))
    print(f"     {result}")

    print("\n3. Тест: 3 числа в диапазоне от -5 до 5:")
    print("   gen_random(3, -5, 5) ->")
    result = list(gen_random(3, -5, 5))
    print(f"     {result}")

    print("\n4. Тест: 1 число (крайний случай):")
    print("   gen_random(1, 100, 100) ->")
    result = list(gen_random(1, 100, 100))
    print(f"     {result}")

    print("\n5. Тест: 0 чисел (пустой результат):")
    print("   gen_random(0, 1, 10) ->")
    result = list(gen_random(0, 1, 10))
    print(f"     {result}")

    print("\n6. Проверка работы как генератора (по одному числу):")
    print("   for num in gen_random(3, 10, 15):")
    for num in gen_random(3, 10, 15):
        print(f"     {num}")


# Для тестирования при запуске файла напрямую
if __name__ == "__main__":
    test_gen_random()
