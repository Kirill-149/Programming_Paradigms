def print_result(func):
    """
    Декоратор для вывода результата выполнения функции.

    Выводит имя функции и результат её выполнения.
    Для list выводит элементы в столбик.
    Для dict выводит пары ключ=значение в столбик.
    Для других типов выводит значение как есть.
    """
    def wrapper(*args, **kwargs):
        # Выполняем оригинальную функцию
        result = func(*args, **kwargs)

        # Выводим имя функции
        print(func.__name__)

        # Выводим результат в зависимости от типа
        if isinstance(result, list):
            for item in result:
                print(item)
        elif isinstance(result, dict):
            for key, value in result.items():
                print(f"{key} = {value}")
        else:
            print(result)

        # Возвращаем результат
        return result

    return wrapper


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')

    # Основные тесты из задания
    test_1()
    test_2()
    test_3()
    test_4()
