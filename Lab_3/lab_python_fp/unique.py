# lab_python_fp/unique.py

class Unique:
    """
    Итератор для удаления дубликатов.

    Args:
        items: Итерируемый объект (список, генератор и т.д.)
        **kwargs: Может содержать параметр ignore_case (bool)
    """
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()
        self.next_item = None

    def __next__(self):
        while True:
            try:
                # Получаем следующий элемент
                item = next(self.items) if self.next_item is None else self.next_item
                self.next_item = None

                # Определяем ключ для сравнения
                if self.ignore_case and isinstance(item, str):
                    key = item.lower()
                else:
                    key = item

                # Проверяем, был ли уже такой элемент
                if key not in self.seen:
                    self.seen.add(key)
                    return item
            except StopIteration:
                raise StopIteration

    def __iter__(self):
        return self


def test_unique():
    """Тестирование итератора Unique"""
    print("Тестирование итератора Unique...")

    # Импортируем gen_random из предыдущей задачи
    try:
        from Lab_3.lab_python_fp.gen_random import gen_random
    except ImportError:
        # Если файл gen_random.py не найден, создадим простую замену
        import random
        def gen_random(num_count, begin, end):
            for _ in range(num_count):
                yield random.randint(begin, end)

    print("\n1. Тест с числами (дубликаты):")
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print(f"   data = {data}")
    print("   Unique(data) ->")
    result = list(Unique(data))
    print(f"     {result}")

    print("\n2. Тест с генератором случайных чисел:")
    data = gen_random(10, 1, 3)
    print("   data = gen_random(10, 1, 3)")
    print("   Unique(data) ->")
    result = list(Unique(data))
    print(f"     {sorted(result)}")  # Сортируем для удобства сравнения

    print("\n3. Тест со строками (без ignore_case):")
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(f"   data = {data}")
    print("   Unique(data) ->")
    result = list(Unique(data))
    print(f"     {result}")

    print("\n4. Тест со строками (с ignore_case=True):")
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(f"   data = {data}")
    print("   Unique(data, ignore_case=True) ->")
    result = list(Unique(data, ignore_case=True))
    print(f"     {result}")

    print("\n5. Тест со смешанными данными:")
    data = [1, '1', 1, '1', 2, '2', 2, '2']
    print(f"   data = {data}")
    print("   Unique(data) ->")
    result = list(Unique(data))
    print(f"     {result}")

    print("\n6. Тест с пустым списком:")
    data = []
    print(f"   data = {data}")
    print("   Unique(data) ->")
    result = list(Unique(data))
    print(f"     {result}")

    print("\n7. Тест с ignore_case=False (по умолчанию):")
    data = ['Python', 'python', 'PYTHON', 'Java', 'java']
    print(f"   data = {data}")
    print("   Unique(data) ->")
    result = list(Unique(data))
    print(f"     {result}")

    print("\n8. Тест с ignore_case=True (явно указан):")
    data = ['Python', 'python', 'PYTHON', 'Java', 'java']
    print(f"   data = {data}")
    print("   Unique(data, ignore_case=True) ->")
    result = list(Unique(data, ignore_case=True))
    print(f"     {result}")

    print("\n9. Тест с разными типами данных:")
    data = [True, 1, 1.0, '1', False, 0, 0.0, '0']
    print(f"   data = {data}")
    print("   Unique(data) ->")
    result = list(Unique(data))
    print(f"     {result}")


# Для тестирования при запуске файла напрямую
if __name__ == "__main__":
    test_unique()
