#!/usr/bin/env python3
"""
Тесты с использованием Mock-объектов
"""

import unittest
from unittest.mock import patch, MagicMock, mock_open
import sys
import io
import math
from main import EquationSolver, main


class TestEquationSolverWithMocks(unittest.TestCase):
    """Тесты с использованием Mock-объектов"""

    def setUp(self):
        self.solver = EquationSolver()

    # Тест 1: Mock для функции input (с заглушкой вывода)
    def test_get_coef_with_input_mock(self):
        """Тестирование get_coef с моком для input"""
        # Мокаем input и print
        with patch('builtins.input', return_value='2.5'):
            with patch('builtins.print'):  # Заглушаем вывод
                result = self.solver.get_coef(4, "Введите коэффициент: ")
                self.assertEqual(result, 2.5)

    # Тест 2: Mock для sys.argv
    def test_get_coef_with_argv_mock(self):
        """Тестирование get_coef с моком для sys.argv"""
        test_argv = ['program.py', '1.0', '2.0', '3.0']

        with patch.object(sys, 'argv', test_argv):
            with patch('builtins.print'):  # Заглушаем возможный вывод
                # Коэффициент из argv
                result = self.solver.get_coef(1, "Введите A: ")
                self.assertEqual(result, 1.0)

    # Тест 3: Mock для math.sqrt с правильными значениями
    def test_solve_equation_with_sqrt_mock(self):
        """Тестирование solve_biquadratic с моком для math.sqrt"""
        # Настраиваем мок для math.sqrt
        with patch('math.sqrt') as mock_sqrt:
            # Задаем поведение мока для уравнения x^4 - 10x^2 + 9 = 0
            # Дискриминант = 100 - 36 = 64 -> sqrt(64) = 8
            # t1 = (10 + 8)/2 = 9 -> sqrt(9) = 3
            # t2 = (10 - 8)/2 = 1 -> sqrt(1) = 1

            def sqrt_side_effect(x):
                if x == 64:
                    return 8.0
                elif x == 9:
                    return 3.0
                elif x == 1:
                    return 1.0
                else:
                    return math.sqrt(x)  # для остальных случаев

            mock_sqrt.side_effect = sqrt_side_effect

            # Уравнение: x^4 - 10x^2 + 9 = 0
            roots = self.solver.solve_biquadratic(1, -10, 9)

            # Проверяем, что sqrt вызывался с правильными аргументами
            # Дискриминант вычисляется внутри solve_quadratic, который вызывается из solve_biquadratic
            mock_sqrt.assert_any_call(64)  # Дискриминант
            mock_sqrt.assert_any_call(9)   # sqrt(t1)
            mock_sqrt.assert_any_call(1)   # sqrt(t2)

    # Тест 4: Mock для проверки вызова функций (исправленный)
    def test_function_calls_with_mock(self):
        """Тестирование последовательности вызовов функций"""
        # Создаем мокированные методы для объекта solver
        mock_solver = MagicMock(spec=EquationSolver)

        # Настраиваем моки
        mock_solver.calculate_discriminant.return_value = 9
        mock_solver.solve_quadratic.return_value = [4, 1]

        # Создаем отдельный мок для math.sqrt
        with patch('math.sqrt') as mock_sqrt:
            mock_sqrt.return_value = 2.0  # sqrt(4) = 2, sqrt(1) = 1, но мы используем одно значение

            # Заменяем статические методы
            with patch.object(EquationSolver, 'calculate_discriminant',
                            side_effect=mock_solver.calculate_discriminant):
                with patch.object(EquationSolver, 'solve_quadratic',
                                side_effect=mock_solver.solve_quadratic):

                    # Вызываем метод
                    roots = self.solver.solve_biquadratic(1, -5, 4)

                    # Проверяем вызовы
                    mock_solver.calculate_discriminant.assert_called_once_with(1, -5, 4)
                    mock_solver.solve_quadratic.assert_called_once_with(1, -5, 4)
                    mock_sqrt.assert_called()

    # Тест 5: Mock для sys.exit с правильными аргументами
    def test_main_with_exit_mock(self):
        """Тестирование main с моком для sys.exit"""
        # Тест с некорректным вводом (a=0)
        # Мокаем sys.argv чтобы передать аргументы
        test_argv = ['test_mock.py', '0', '1', '1']

        with patch.object(sys, 'argv', test_argv):
            with patch('sys.exit') as mock_exit:
                with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                    # Запускаем main
                    main()

                    # Проверяем вывод
                    output = mock_stdout.getvalue()
                    self.assertIn("а=0", output)

                    # Проверяем, что sys.exit вызывался с кодом 1
                    mock_exit.assert_called_with(1)

    # Тест 6: Integration test с моками (упрощенный)
    def test_integration_with_mocks(self):
        """Интеграционный тест с использованием моков"""
        # Мокаем все вводы/выводы
        test_argv = ['test_mock.py', '1', '-5', '4']

        with patch.object(sys, 'argv', test_argv):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                # Запускаем main
                main()

                # Получаем вывод
                output = mock_stdout.getvalue()

                # Проверяем, что вывод содержит корни
                self.assertIn("Корень уравнения:", output)
                # Уравнение x^4 - 5x^2 + 4 = 0 имеет корни -2, -1, 1, 2
                self.assertIn("2.000000", output)
                self.assertIn("-2.000000", output)


class TestQuadraticSolverWithMocks(unittest.TestCase):
    """Тесты для квадратного решателя с моками"""

    def setUp(self):
        self.solver = EquationSolver()

    def test_solve_quadratic_with_negative_discriminant(self):
        """Тестирование solve_quadratic с отрицательным дискриминантом"""
        # Мокаем calculate_discriminant
        with patch.object(self.solver, 'calculate_discriminant', return_value=-4):
            roots = self.solver.solve_quadratic(1, 2, 5)
            self.assertEqual(roots, [])

    def test_solve_quadratic_with_zero_discriminant(self):
        """Тестирование solve_quadratic с нулевым дискриминантом"""
        with patch.object(self.solver, 'calculate_discriminant', return_value=0):
            roots = self.solver.solve_quadratic(1, -4, 4)
            self.assertEqual(len(roots), 1)
            self.assertEqual(roots[0], 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
