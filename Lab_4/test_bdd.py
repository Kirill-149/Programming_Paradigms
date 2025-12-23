#!/usr/bin/env python3
"""
BDD тесты для решения биквадратных уравнений (без pytest)
"""

import unittest
import math
from main import EquationSolver


class TestEquationSolverBDD(unittest.TestCase):
    """BDD-стиль тестов для EquationSolver"""

    def setUp(self):
        self.solver = EquationSolver()

    # Сценарий 1: Решение уравнения с четырьмя корнями
    def test_equation_with_four_real_roots(self):
        """
        Сценарий: Решение уравнения с четырьмя действительными корнями

        Given: уравнение с коэффициентами A=1, B=-5, C=4
        When: я решаю биквадратное уравнение
        Then: я получаю 4 действительных корней
        And: корни равны -2, -1, 1, 2
        """
        # Given
        a, b, c = 1, -5, 4

        # When
        roots = self.solver.solve_biquadratic(a, b, c)

        # Then
        self.assertEqual(len(roots), 4, f"Ожидалось 4 корня, получено {len(roots)}")

        # And
        expected_roots = [-2, -1, 1, 2]
        for expected, actual in zip(expected_roots, roots):
            self.assertAlmostEqual(actual, expected, places=6,
                                 msg=f"Ожидался корень {expected}, получен {actual}")

    # Сценарий 2: Решение уравнения без действительных корней
    def test_equation_without_real_roots(self):
        """
        Сценарий: Решение уравнения без действительных корней

        Given: уравнение с коэффициентами A=1, B=1, C=1
        When: я решаю биквадратное уравнение
        Then: я получаю пустой список корней
        """
        # Given
        a, b, c = 1, 1, 1

        # When
        roots = self.solver.solve_biquadratic(a, b, c)

        # Then
        self.assertEqual(len(roots), 0, f"Ожидался пустой список, получено {len(roots)} корней")

    # Сценарий 3: Решение уравнения с нулевым коэффициентом A
    def test_equation_with_zero_coefficient_a(self):
        """
        Сценарий: Решение уравнения с нулевым коэффициентом A

        Given: уравнение с коэффициентами A=0, B=1, C=1
        When: я решаю биквадратное уравнение
        Then: я получаю ошибку "Коэффициент а=0, это не квадратное уравнение"
        """
        # Given
        a, b, c = 0, 1, 1

        # When / Then
        with self.assertRaises(ValueError) as context:
            self.solver.solve_biquadratic(a, b, c)

        # Then
        self.assertIn("а=0", str(context.exception),
                     f"Ожидалось сообщение об ошибке с 'а=0', получено: {context.exception}")

    # Сценарий 4: Решение уравнения с одним корнем (нулевым)
    def test_equation_with_single_zero_root(self):
        """
        Сценарий: Решение уравнения с одним нулевым корнем

        Given: уравнение с коэффициентами A=1, B=0, C=0
        When: я решаю биквадратное уравнение
        Then: я получаю 1 действительный корень
        And: единственный корень равен 0
        """
        # Given
        a, b, c = 1, 0, 0

        # When
        roots = self.solver.solve_biquadratic(a, b, c)

        # Then
        self.assertEqual(len(roots), 1, f"Ожидался 1 корень, получено {len(roots)}")

        # And
        self.assertAlmostEqual(roots[0], 0, places=6,
                             msg=f"Ожидался корень 0, получен {roots[0]}")

    # Сценарий 5: Решение уравнения с двумя корнями
    def test_equation_with_two_roots(self):
        """
        Сценарий: Решение уравнения с двумя корнями

        Given: уравнение с коэффициентами A=1, B=0, C=-9
        When: я решаю биквадратное уравнение
        Then: я получаю 2 действительных корня
        And: корни равны -√3, √3
        """
        # Given
        a, b, c = 1, 0, -9

        # When
        roots = self.solver.solve_biquadratic(a, b, c)

        # Then
        self.assertEqual(len(roots), 2, f"Ожидалось 2 корня, получено {len(roots)}")

        # And
        expected_roots = [-math.sqrt(3), math.sqrt(3)]
        for expected, actual in zip(expected_roots, roots):
            self.assertAlmostEqual(actual, expected, places=6,
                                 msg=f"Ожидался корень {expected}, получен {actual}")

    # Сценарий 6: Форматирование решения
    def test_format_solution(self):
        """
        Сценарий: Форматирование решения уравнения

        Given: уравнение имеет корни [-2, -1, 1, 2] и дискриминант 9
        When: я форматирую решение
        Then: получаю отформатированную строку с корнями
        """
        # Given
        roots = [-2.0, -1.0, 1.0, 2.0]
        D = 9.0

        # When
        result = self.solver.format_solution(roots, D)

        # Then
        self.assertIn("Корень уравнения:", result)
        self.assertIn("-2.000000", result)
        self.assertIn("2.000000", result)
        # Проверяем, что 4 строки с корнями
        lines = result.strip().split('\n')
        self.assertEqual(len(lines), 4)


def run_all_bdd_tests():
    """Запуск всех BDD тестов с красивым выводом"""
    print("Запуск BDD тестов для биквадратных уравнений")
    print("="*60)

    # Создаем тестовый набор
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestEquationSolverBDD)

    # Запускаем тесты
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Выводим статистику в BDD-стиле
    print("\n" + "="*60)
    print("Сводка по BDD сценариям:")
    print("="*60)

    # Список тестов и их описаний
    test_scenarios = [
        ("Уравнение с четырьмя корнями", "test_equation_with_four_real_roots"),
        ("Уравнение без корней", "test_equation_without_real_roots"),
        ("Уравнение с a=0", "test_equation_with_zero_coefficient_a"),
        ("Уравнение с нулевым корнем", "test_equation_with_single_zero_root"),
        ("Уравнение с двумя корнями", "test_equation_with_two_roots"),
        ("Форматирование решения", "test_format_solution"),
    ]

    # Создаем словарь результатов
    results_dict = {}
    for _, test_method in test_scenarios:
        results_dict[test_method] = "PASS"

    for failure in result.failures:
        test_method = failure[0]._testMethodName
        results_dict[test_method] = "FAIL"

    for error in result.errors:
        test_method = error[0]._testMethodName
        results_dict[test_method] = "ERROR"

    # Выводим результаты
    passed = 0
    for scenario_name, test_method in test_scenarios:
        status = results_dict.get(test_method, "NOT RUN")
        status_symbol = "✓" if status == "PASS" else "✗"
        print(f"{status_symbol} {scenario_name}: {status}")
        if status == "PASS":
            passed += 1

    print(f"\nВсего сценариев: {len(test_scenarios)}")
    print(f"Пройдено: {passed}")
    print(f"Не пройдено: {len(test_scenarios) - passed}")
    print("="*60)

    if result.wasSuccessful():
        print("Все BDD сценарии успешно пройдены!")
    else:
        print("Некоторые BDD сценарии не пройдены")

    return result.wasSuccessful()


if __name__ == '__main__':
    run_all_bdd_tests()
