# lab_python_fp/field.py

def field(items, *args):
    """
    Генератор для извлечения значений из словарей.

    Args:
        items: Список словарей
        *args: Ключи для извлечения

    Yields:
        Значение ключа или словарь с указанными ключами

    Raises:
        AssertionError: Если не передано ни одного ключа
    """
    assert len(args) > 0, "Должен быть передан хотя бы один аргумент для извлечения"

    # Если передан только один аргумент
    if len(args) == 1:
        key = args[0]
        for item in items:
            if key in item and item[key] is not None:
                yield item[key]

    # Если передано несколько аргументов
    else:
        for item in items:
            # Создаем временный словарь для результата
            result = {}

            # Заполняем словарь значениями, если они не None
            for key in args:
                if key in item and item[key] is not None:
                    result[key] = item[key]

            # Если в результате есть хотя бы один ключ - выдаем его
            if result:
                yield result


def test_field():
    """Тестирование генератора field"""
    print("Тестирование генератора field...")

    # Тестовые данные
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'},
        {'title': None, 'price': 1500, 'color': 'red'},
        {'price': 3000, 'color': 'blue'},
        {'title': None, 'price': None, 'color': None},
        {},
    ]

    print("\n1. Тест с одним аргументом:")
    print("   field(goods, 'title') ->")
    result = list(field(goods, 'title'))
    for item in result:
        print(f"     '{item}'")

    print("\n2. Тест с несколькими аргументами:")
    print("   field(goods, 'title', 'price') ->")
    result = list(field(goods, 'title', 'price'))
    for item in result:
        print(f"     {item}")

    print("\n3. Тест с аргументами, где все значения None:")
    print("   field(goods, 'title', 'color') ->")
    result = list(field(goods, 'title', 'color'))
    for item in result:
        print(f"     {item}")

    print("\n4. Тест с несуществующими ключами:")
    print("   field(goods, 'title', 'weight') ->")
    result = list(field(goods, 'title', 'weight'))
    for item in result:
        print(f"     {item}")

    print("\n5. Тест с пустым списком:")
    print("   field([], 'title') ->")
    result = list(field([], 'title'))
    print(f"     {result}")

    print("\n6. Пример из задания (точный пример):")
    goods_example = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'}
    ]

    print("   field(goods_example, 'title') ->")
    result = list(field(goods_example, 'title'))
    for item in result:
        print(f"     '{item}'")

    print("\n   field(goods_example, 'title', 'price') ->")
    result = list(field(goods_example, 'title', 'price'))
    for item in result:
        print(f"     {item}")

    print("\n7. Дополнительный тест с None значениями (из описания задания):")
    goods_with_none = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': None, 'color': 'black'}
    ]

    print("   field(goods_with_none, 'title', 'price') ->")
    result = list(field(goods_with_none, 'title', 'price'))
    for item in result:
        print(f"     {item}")


# Для тестирования при запуске файла напрямую
if __name__ == "__main__":
    test_field()
