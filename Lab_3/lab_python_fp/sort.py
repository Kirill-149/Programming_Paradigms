data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    # Способ 1: Без использования lambda-функции
    result = sorted(data, key=abs, reverse=True)
    print("Без lambda:", result)

    # Способ 2: С использованием lambda-функции
    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    print("С lambda:", result_with_lambda)

    # Проверка, что результаты одинаковые
    assert result == result_with_lambda, "Результаты должны быть одинаковыми"

    # Пример из задания для проверки
    print("\nПроверка по примеру из задания:")
    expected = [123, 100, -100, -30, 30, 4, -4, 1, -1, 0]
    print("Ожидаемый результат:", expected)
    print("Фактический результат:", result)
    print("Результаты совпадают:", result == expected)
