import unittest
import sys
import os
import math

# Добавляем путь к пакету
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from equation_solver.biquadratic import BiquadraticSolver, InputHandler


class TestBiquadraticSolverTDD(unittest.TestCase):
    """TDD тесты для решения биквадратных уравнений"""

    def test_validate_coefficients_valid_input(self):
        """Тест валидации корректных коэффициентов"""
        is_valid, error = BiquadraticSolver.validate_coefficients(1, 2, 3)
        self.assertTrue(is_valid)
        self.assertIsNone(error)

    def test_validate_coefficients_zero_a(self):
        """Тест валидации при a=0"""
        is_valid, error = BiquadraticSolver.validate_coefficients(0, 2, 3)
        self.assertFalse(is_valid)
        self.assertEqual(error, "Коэффициент A не может быть равен 0 (это не биквадратное уравнение)")

    def test_validate_coefficients_non_numeric(self):
        """Тест валидации нечисловых коэффициентов"""
        is_valid, error = BiquadraticSolver.validate_coefficients("abc", 2, 3)
        self.assertFalse(is_valid)
        self.assertEqual(error, "Коэффициент A должен быть числом")

    def test_solve_simple_biquadratic(self):
        """Тест решения простого биквадратного уравнения x^4 - 5x^2 + 4 = 0"""
        # Уравнение: x^4 - 5x^2 + 4 = 0
        # Замена: t = x^2, тогда t^2 - 5t + 4 = 0
        # Корни: t1 = 4, t2 = 1
        # x = ±√4 = ±2, x = ±√1 = ±1
        roots, message = BiquadraticSolver.solve(1, -5, 4)

        expected_roots = [-2, -1, 1, 2]
        self.assertEqual(len(roots), 4)

        for expected in expected_roots:
            found = False
            for root in roots:
                if math.isclose(root, expected, rel_tol=1e-9):
                    found = True
                    break
            self.assertTrue(found, f"Корень {expected} не найден")

    def test_solve_no_real_roots(self):
        """Тест решения уравнения без действительных корней x^4 + x^2 + 1 = 0"""
        # Уравнение: x^4 + x^2 + 1 = 0
        # Дискриминант: 1 - 4 = -3 < 0
        roots, message = BiquadraticSolver.solve(1, 1, 1)

        self.assertEqual(len(roots), 0)
        self.assertEqual(message, "Нет действительных корней (дискриминант отрицательный)")

    def test_solve_double_root(self):
        """Тест решения уравнения с двойным корнем x^4 - 2x^2 + 1 = 0"""
        # Уравнение: x^4 - 2x^2 + 1 = 0
        # (x^2 - 1)^2 = 0
        # x^2 = 1 => x = ±1
        roots, message = BiquadraticSolver.solve(1, -2, 1)

        expected_roots = [-1, 1]
        self.assertEqual(len(roots), 2)

        for expected in expected_roots:
            self.assertTrue(any(math.isclose(root, expected, rel_tol=1e-9) for root in roots))

    def test_solve_zero_root(self):
        """Тест решения уравнения с корнем 0 x^4 - 3x^2 = 0"""
        # Уравнение: x^4 - 3x^2 = 0
        # x^2(x^2 - 3) = 0
        # x = 0, x = ±√3
        roots, message = BiquadraticSolver.solve(1, -3, 0)

        expected_roots = [-math.sqrt(3), 0, math.sqrt(3)]
        self.assertEqual(len(roots), 3)

        for expected in expected_roots:
            self.assertTrue(any(math.isclose(root, expected, rel_tol=1e-9) for root in roots))

    def test_solve_only_zero_root(self):
        """Тест решения уравнения только с корнем 0 x^4 = 0"""
        roots, message = BiquadraticSolver.solve(1, 0, 0)

        self.assertEqual(len(roots), 1)
        self.assertTrue(math.isclose(roots[0], 0, rel_tol=1e-9))

    def test_solve_complex_case(self):
        """Тест решения сложного случая x^4 - 13x^2 + 36 = 0"""
        # Уравнение: x^4 - 13x^2 + 36 = 0
        # Корни: x = ±2, x = ±3
        roots, message = BiquadraticSolver.solve(1, -13, 36)

        expected_roots = [-3, -2, 2, 3]
        self.assertEqual(len(roots), 4)

        for expected in expected_roots:
            self.assertTrue(any(math.isclose(root, expected, rel_tol=1e-9) for root in roots))

    def test_solve_with_negative_t_values(self):
        """Тест решения когда оба t отрицательные"""
        # Уравнение: x^4 + 5x^2 + 6 = 0
        # t^2 + 5t + 6 = 0, корни: t = -2, t = -3 (оба отрицательные)
        roots, message = BiquadraticSolver.solve(1, 5, 6)

        self.assertEqual(len(roots), 0)
        self.assertEqual(message, "Нет действительных корней")

    def test_solve_mixed_t_values(self):
        """Тест решения когда один t положительный, другой отрицательный"""
        # Уравнение: x^4 - 2x^2 - 3 = 0
        # t^2 - 2t - 3 = 0, корни: t = 3, t = -1
        # x = ±√3
        roots, message = BiquadraticSolver.solve(1, -2, -3)

        expected_roots = [-math.sqrt(3), math.sqrt(3)]
        self.assertEqual(len(roots), 2)

        for expected in expected_roots:
            self.assertTrue(any(math.isclose(root, expected, rel_tol=1e-9) for root in roots))


class TestInputHandlerTDD(unittest.TestCase):
    """TDD тесты для обработки ввода"""

    def test_get_coef_valid_float(self):
        """Тест получения корректного float коэффициента"""
        # Здесь мы не можем легко протестировать sys.argv,
        # но можем проверить что метод существует
        self.assertTrue(hasattr(InputHandler, 'get_coef'))
        self.assertTrue(callable(InputHandler.get_coef))

    def test_input_handler_structure(self):
        """Тест структуры класса InputHandler"""
        self.assertTrue(hasattr(InputHandler, 'get_coef'))
        self.assertIsInstance(InputHandler.get_coef, staticmethod)


if __name__ == '__main__':
    unittest.main(verbosity=2)
