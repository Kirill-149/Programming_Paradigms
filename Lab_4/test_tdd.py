#!/usr/bin/env python3
"""
TDD тесты для решения биквадратных уравнений
"""

import unittest
import math
from main import EquationSolver


class TestEquationSolverTDD(unittest.TestCase):
    """TDD тесты для класса EquationSolver"""

    def setUp(self):
        """Настройка тестового окружения"""
        self.solver = EquationSolver()

    def test_simple_equation(self):
        """
        Тестирование уравнения: x^4 - 5x^2 + 4 = 0
        Ожидаемые корни: -2, -1, 1, 2
        """
        a, b, c = 1, -5, 4
        roots = self.solver.solve_biquadratic(a, b, c)

        self.assertEqual(len(roots), 4)

        expected_roots = [-2, -1, 1, 2]
        for expected, actual in zip(expected_roots, roots):
            self.assertAlmostEqual(actual, expected, places=6)

    def test_equation_with_zero_root(self):
        """Тестирование уравнения: x^4 = 0"""
        a, b, c = 1, 0, 0
        roots = self.solver.solve_biquadratic(a, b, c)

        self.assertEqual(len(roots), 1)
        self.assertAlmostEqual(roots[0], 0, places=6)

    def test_equation_without_real_roots(self):
        """Тестирование уравнения: x^4 + x^2 + 1 = 0"""
        a, b, c = 1, 1, 1
        roots = self.solver.solve_biquadratic(a, b, c)

        self.assertEqual(len(roots), 0)

    def test_equation_with_two_roots(self):
        """Тестирование уравнения: x^4 - 9 = 0"""
        a, b, c = 1, 0, -9
        roots = self.solver.solve_biquadratic(a, b, c)

        self.assertEqual(len(roots), 2)

        expected = [-math.sqrt(3), math.sqrt(3)]
        for exp, act in zip(expected, roots):
            self.assertAlmostEqual(act, exp, places=6)

    def test_discriminant_calculation(self):
        """Тестирование правильности вычисления дискриминанта"""
        test_cases = [
            (1, -5, 4, 9),   # D > 0
            (1, -4, 4, 0),   # D = 0
            (1, 2, 5, -16),  # D < 0
        ]

        for a, b, c, expected in test_cases:
            D = self.solver.calculate_discriminant(a, b, c)
            self.assertAlmostEqual(D, expected, places=6)

    def test_zero_coefficient_a(self):
        """Тестирование обработки случая a = 0"""
        with self.assertRaises(ValueError) as context:
            self.solver.solve_biquadratic(0, 1, 1)

        self.assertIn("а=0", str(context.exception))


class TestQuadraticSolverTDD(unittest.TestCase):
    """TDD тесты для решения квадратных уравнений"""

    def setUp(self):
        self.solver = EquationSolver()

    def test_quadratic_two_roots(self):
        """Квадратное уравнение с двумя корнями"""
        roots = self.solver.solve_quadratic(1, -5, 4)
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(roots[0], 4, places=6)
        self.assertAlmostEqual(roots[1], 1, places=6)

    def test_quadratic_one_root(self):
        """Квадратное уравнение с одним корнем"""
        roots = self.solver.solve_quadratic(1, -4, 4)
        self.assertEqual(len(roots), 1)
        self.assertAlmostEqual(roots[0], 2, places=6)

    def test_quadratic_no_roots(self):
        """Квадратное уравнение без корней"""
        roots = self.solver.solve_quadratic(1, 2, 5)
        self.assertEqual(len(roots), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
