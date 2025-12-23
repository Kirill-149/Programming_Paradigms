import unittest
from main import (
    Computer, DisplayClass, ComputerDisplayClass,
    ComputerService, create_sample_data
)


class TestComputerService(unittest.TestCase):
    """Тесты для сервиса работы с компьютерами"""

    def setUp(self):
        """Настройка тестовых данных перед каждым тестом"""
        self.computers, self.display_classes, self.computer_display_classes = create_sample_data()
        self.service = ComputerService(
            self.computers,
            self.display_classes,
            self.computer_display_classes
        )

    def test_get_computers_in_class_a(self):
        """
        Тест для задания Г1:
        Проверяем, что возвращаются только классы на 'А'
        и правильные компьютеры в них
        """
        result = self.service.get_computers_in_class_a()

        # Проверяем, что все ключи начинаются на 'А'
        for class_name in result.keys():
            self.assertTrue(class_name.startswith('А'),
                          f"Класс {class_name} должен начинаться с 'А'")

        # Проверяем наличие ожидаемых классов
        expected_classes = {'А-101', 'А-303', 'А-505'}
        self.assertEqual(set(result.keys()), expected_classes)

        # Проверяем количество компьютеров в классе А-303
        self.assertEqual(len(result['А-303']), 3)

        # Проверяем модели в классе А-303
        models = [comp.model for comp in result['А-303']]
        expected_models = ['Lenovo ThinkCentre', 'Acer Veriton', 'Asus ExpertCenter']
        self.assertListEqual(sorted(models), sorted(expected_models))

    def test_get_max_price_per_class(self):
        """
        Тест для задания Г2:
        Проверяем правильность расчета максимальных цен
        """
        result = self.service.get_max_price_per_class()

        # Результат должен быть отсортирован по убыванию максимальной цены
        prices = [price for _, price in result]
        self.assertEqual(prices, sorted(prices, reverse=True))

        # Проверяем конкретные значения
        result_dict = dict(result)

        # В классе А-303 максимальная цена 60000 (Lenovo ThinkCentre)
        self.assertEqual(result_dict['А-303'], 60000)

        # В классе А-505 максимальная цена 52000 (MSI Pro)
        self.assertEqual(result_dict['А-505'], 52000)

        # В классе А-101 максимальная цена 50000 (Dell Optiplex)
        self.assertEqual(result_dict['А-101'], 50000)

        # В классе Б-202 максимальная цена 45000 (HP ProDesk)
        self.assertEqual(result_dict['Б-202'], 45000)

        # Класс В-404 не должен присутствовать, так как в нем нет компьютеров
        self.assertNotIn('В-404', result_dict)

        # Проверяем количество классов с компьютерами (4 из 5)
        self.assertEqual(len(result), 4)

    def test_get_all_computer_display_connections(self):
        """
        Тест для задания Г3:
        Проверяем все связи (один-ко-многим + многие-ко-многим)
        """
        result = self.service.get_all_computer_display_connections()

        # Проверяем сортировку по названию класса
        class_names = list(result.keys())
        self.assertEqual(class_names, sorted(class_names))

        # Должны быть ВСЕ 5 классов, включая В-404 (даже пустой)
        expected_classes = {'А-101', 'А-303', 'А-505', 'Б-202', 'В-404'}
        self.assertEqual(set(result.keys()), expected_classes)

        # Проверяем сортировку компьютеров внутри классов по убыванию цены
        for class_name, computers in result.items():
            prices = [comp.price for comp in computers]
            self.assertEqual(prices, sorted(prices, reverse=True),
                           f"Компьютеры в классе {class_name} должны быть отсортированы по убыванию цены")

        # Проверяем конкретные классы

        # В-404 должен быть пустым
        self.assertEqual(len(result['В-404']), 0)

        # А-101 должен иметь 2 компьютера (Dell + Lenovo из доп. связи)
        self.assertEqual(len(result['А-101']), 2)

        # Б-202 должен иметь 2 компьютера (HP + Asus из доп. связи)
        self.assertEqual(len(result['Б-202']), 2)

        # А-303 должен иметь 3 компьютера
        self.assertEqual(len(result['А-303']), 3)

        # А-505 должен иметь 2 компьютера
        self.assertEqual(len(result['А-505']), 2)

        # Проверяем, что в А-101 есть оба компьютера
        models_a101 = [comp.model for comp in result['А-101']]
        self.assertIn('Dell Optiplex', models_a101)
        self.assertIn('Lenovo ThinkCentre', models_a101)

        # Проверяем, что в Б-202 есть оба компьютера
        models_b202 = [comp.model for comp in result['Б-202']]
        self.assertIn('HP ProDesk', models_b202)
        self.assertIn('Asus ExpertCenter', models_b202)

        # Проверяем общее количество связей
        total_connections = sum(len(computers) for computers in result.values())
        self.assertEqual(total_connections, 9)  # 7 основных + 2 дополнительные


class TestComputerServiceEdgeCases(unittest.TestCase):
    """Тесты для граничных случаев"""

    def test_empty_data(self):
        """Тест с пустыми данными"""
        service = ComputerService([], [], [])

        result1 = service.get_computers_in_class_a()
        result2 = service.get_max_price_per_class()
        result3 = service.get_all_computer_display_connections()

        self.assertEqual(result1, {})
        self.assertEqual(result2, [])
        self.assertEqual(result3, {})

    def test_no_class_a(self):
        """Тест когда нет классов на букву 'А'"""
        display_classes = [
            DisplayClass(1, 'Б-101'),
            DisplayClass(2, 'В-202'),
        ]

        computers = [
            Computer(1, 'Test Model', 10000, 1),
        ]

        service = ComputerService(computers, display_classes)
        result = service.get_computers_in_class_a()

        self.assertEqual(result, {})


if __name__ == '__main__':
    unittest.main(verbosity=2)
