#!/usr/bin/env python3
"""
Программа для решения биквадратных уравнений вида a*x^4 + b*x^2 + c = 0
"""

import sys
import math


class EquationSolver:  # Было: BiquadraticEquationSolver
    """Класс для решения биквадратных уравнений"""

    @staticmethod
    def get_coef(index: int, prompt: str) -> float:
        """
        Получает коэффициент из аргументов командной строки или запрашивает ввод

        Args:
            index: Индекс в sys.argv
            prompt: Сообщение для запроса ввода

        Returns:
            Значение коэффициента
        """
        try:
            coef_str = sys.argv[index]
        except IndexError:
            print(prompt)
            coef_str = input()
        return float(coef_str)

    @staticmethod
    def calculate_discriminant(a: float, b: float, c: float) -> float:
        """Вычисляет дискриминант квадратного уравнения относительно t = x^2"""
        return b * b - 4 * a * c

    @staticmethod
    def solve_quadratic(a: float, b: float, c: float) -> list:
        """
        Решает квадратное уравнение a*t^2 + b*t + c = 0

        Returns:
            Список действительных корней
        """
        D = EquationSolver.calculate_discriminant(a, b, c)

        if D < 0:
            return []
        elif D == 0:
            t = -b / (2 * a)
            return [t]
        else:
            sqrt_D = math.sqrt(D)
            t1 = (-b + sqrt_D) / (2 * a)
            t2 = (-b - sqrt_D) / (2 * a)
            return [t1, t2]

    @staticmethod
    def solve_biquadratic(a: float, b: float, c: float) -> list:
        """
        Решает биквадратное уравнение a*x^4 + b*x^2 + c = 0

        Returns:
            Список действительных корней x (в порядке возрастания)
        """
        if a == 0:
            raise ValueError("Коэффициент а=0, это не квадратное уравнение")

        # Решаем квадратное уравнение относительно t = x^2
        t_roots = EquationSolver.solve_quadratic(a, b, c)
        x_roots = []

        for t in t_roots:
            if t > 0:
                x_roots.append(math.sqrt(t))
                x_roots.append(-math.sqrt(t))
            elif t == 0:
                x_roots.append(0.0)
            # t < 0 - не дает действительных корней

        # Сортируем корни по возрастанию
        x_roots.sort()
        return x_roots

    @staticmethod
    def format_solution(roots: list, D: float) -> str:
        """
        Форматирует решение для вывода в консоль

        Returns:
            Отформатированная строка с решением
        """
        if D < 0:
            return "Нет корней (дискриминант отрицательный)"

        if not roots:
            return "Нет действительных корней"

        result = []
        for root in roots:
            # Для корня 0 выводим без знака минус
            if root == 0:
                result.append("Корень уравнения: 0")
            else:
                result.append(f"Корень уравнения: {root:.6f}")

        return "\n".join(result)


def main():
    """Основная функция программы"""
    solver = EquationSolver()

    try:
        # Получаем коэффициенты
        a = solver.get_coef(1, "Введите A: ")
        b = solver.get_coef(2, "Введите B: ")
        c = solver.get_coef(3, "Введите C: ")

        # Решаем уравнение
        roots = solver.solve_biquadratic(a, b, c)

        # Вычисляем дискриминант для форматирования
        D = solver.calculate_discriminant(a, b, c)

        # Форматируем и выводим результат
        solution = solver.format_solution(roots, D)
        print(solution)

    except ValueError as e:
        print(str(e))
        sys.exit(1)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
