from operator import itemgetter

class Computer:
    """Компьютер"""
    def __init__(self, id, model, price, display_class_id):
        self.id = id
        self.model = model
        self.price = price
        self.display_class_id = display_class_id

class DisplayClass:
    """Дисплейный класс"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class ComputerDisplayClass:
    """Компьютеры в дисплейных классах для связи многие-ко-многим"""
    def __init__(self, display_class_id, computer_id):
        self.display_class_id = display_class_id
        self.computer_id = computer_id

# Дисплейные классы
display_classes = [
    DisplayClass(1, 'А-101'),
    DisplayClass(2, 'Б-202'),
    DisplayClass(3, 'А-303'),
    DisplayClass(4, 'В-404'),
    DisplayClass(5, 'А-505'),
]

# Компьютеры
computers = [
    Computer(1, 'Dell Optiplex', 50000, 1),      # А-101
    Computer(2, 'HP ProDesk', 45000, 2),         # Б-202
    Computer(3, 'Lenovo ThinkCentre', 60000, 3), # А-303
    Computer(4, 'Acer Veriton', 40000, 3),       # А-303
    Computer(5, 'Asus ExpertCenter', 55000, 3),  # А-303
    Computer(6, 'Fujitsu Esprimo', 48000, 5),    # А-505
    Computer(7, 'MSI Pro', 52000, 5),            # А-505
]

# Связь многие-ко-многим (дополнительные связи)
computers_display_classes = [
    ComputerDisplayClass(1, 3),  # Lenovo в А-101 (дополнительно)
    ComputerDisplayClass(2, 5),  # Asus в Б-202 (дополнительно)
]

def main():
    """Основная функция"""

    print('Задание Г1')
    print('Список всех дисплейных классов, у которых название начинается с буквы «А», и список компьютеров в них:')

    # ЗАДАНИЕ Г1: связь один-ко-многим
    one_to_many = [(c, dc) for dc in display_classes for c in computers if c.display_class_id == dc.id]

    result_1 = {}
    for computer, display_class in one_to_many:
        if display_class.name.startswith('А'):
            if display_class.name not in result_1:
                result_1[display_class.name] = []
            result_1[display_class.name].append(computer)

    for class_name, comp_list in sorted(result_1.items()):
        print(f"\n{class_name}:")
        for comp in comp_list:
            print(f"  - {comp.model} (цена: {comp.price} руб.)")

    print('\n' + '='*60)
    print('Задание Г2')
    print('Список дисплейных классов с максимальной ценой компьютеров в каждом классе, отсортированный по максимальной цене:')

    # ЗАДАНИЕ Г2: связь один-ко-многим
    class_computers = {}
    for computer, display_class in one_to_many:
        if display_class.name not in class_computers:
            class_computers[display_class.name] = []
        class_computers[display_class.name].append(computer.price)

    max_prices = {}
    for class_name, prices in class_computers.items():
        max_prices[class_name] = max(prices)

    result_2 = sorted(max_prices.items(), key=itemgetter(1), reverse=True)

    for class_name, max_price in result_2:
        print(f"{class_name}: {max_price} руб.")

    print('\n' + '='*60)
    print('Задание Г3')
    print('Список всех связанных компьютеров и дисплейных классов, отсортированный по классам:')

    # ЗАДАНИЕ Г3: ВСЕ связи (один-ко-многим + многие-ко-многим)
    all_connections = []

    # 1. Добавляем все связи один-ко-многим
    for computer, display_class in one_to_many:
        all_connections.append((computer, display_class))

    # 2. Добавляем все связи многие-ко-многим
    for cdc in computers_display_classes:
        computer = next((c for c in computers if c.id == cdc.computer_id), None)
        display_class = next((dc for dc in display_classes if dc.id == cdc.display_class_id), None)
        if computer and display_class:
            # Проверяем, нет ли уже такой связи в all_connections
            connection_exists = any(
                conn[0].id == computer.id and conn[1].id == display_class.id
                for conn in all_connections
            )
            if not connection_exists:
                all_connections.append((computer, display_class))

    # Сортируем по названию класса (основная сортировка)
    all_connections.sort(key=lambda x: x[1].name)

    # Группируем по классам
    result_3 = {}
    for computer, display_class in all_connections:
        if display_class.name not in result_3:
            result_3[display_class.name] = []
        result_3[display_class.name].append(computer)

    # Для каждого класса сортируем компьютеры произвольно (по убыванию цены)
    for class_name, comp_list in sorted(result_3.items()):
        comp_list_sorted = sorted(comp_list, key=lambda x: x.price, reverse=True)
        print(f"\n{class_name}:")
        for comp in comp_list_sorted:
            print(f"  - {comp.model} (цена: {comp.price} руб.)")

if __name__ == '__main__':
    main()
