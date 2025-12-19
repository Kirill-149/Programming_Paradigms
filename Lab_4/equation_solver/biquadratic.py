"""
Модуль для решения биквадратных уравнений вида ax^4 + bx^2 + c = 0
"""
import sys
import math
from typing import List, Tuple, Optional, Union


class InputHandler:
    """Класс для обработки ввода коэффициентов"""

    @staticmethod
    def get_coef(index: int, prompt: str) -> float:
        """
        Получение коэффициента из аргументов командной строки или ввода пользователя

        Args:
            index: Индекс аргумента командной строки
            prompt: Сообщение для пользователя при вводе с клавиатуры

        Returns:
            Значение коэффициента как float
        """
        try:
            coef_str = sys.argv[index]
        except IndexError:
            print(prompt)
            coef_str = input()

        try:
            return float(coef_str)
        except ValueError:
            raise ValueError(f"Неверный формат числа: {coef_str}")


class BiquadraticSolver:
    """Класс для решения биквадратных уравнений"""

    @staticmethod
    def validate_coefficients(a: float, b: float, c: float) -> Tuple[bool, Optional[str]]:
        """
        Проверка валидности коэффициентов

        Args:
            a: Коэффициент при x^4
            b: Коэффициент при x^2
            c: Свободный член

        Returns:
            Кортеж (is_valid, error_message)
        """
        if not isinstance(a, (int, float)):
            return False, "Коэффициент A должен быть числом"
        if not isinstance(b, (int, float)):
            return False, "Коэффициент B должен быть числом"
        if not isinstance(c, (int, float)):
            return False, "Коэффициент C должен быть числом"

        if a == 0:
            return False, "Коэффициент A не может быть равен 0 (это не биквадратное уравнение)"

        return True, None

    @staticmethod
    def solve(a: float, b: float, c: float) -> Tuple[List[float], str]:
        """
        Решение биквадратного уравнения ax^4 + bx^2 + c = 0

        Args:
            a: Коэффициент при x^4
            b: Коэффициент при x^2
            c: Свободный член

        Returns:
            Кортеж (roots, message) где:
            - roots: список действительных корней
            - message: текстовое описание результата
        """
        # Валидация коэффициентов
        is_valid, error = BiquadraticSolver.validate_coefficients(a, b, c)
        if not is_valid:
            return [], error

        # Вычисление дискриминанта
        D = b*b - 4*a*c
        roots = []

        if D < 0.0:
            return [], "Нет действительных корней (дискриминант отрицательный)"

        elif D == 0.0:
            t0 = -b / (2*a)
            if t0 > 0.0:
                root1 = math.sqrt(t0)
                root2 = -math.sqrt(t0)
                roots.extend([root1, root2])
                return roots, f"Два корня: {root1:.4f} и {root2:.4f}"
            elif t0 == 0.0:
                roots.append(0.0)
                return roots, "Один корень: 0"
            else:
                return [], "Нет действительных корней (t0 отрицательный)"

        else:  # D > 0
            sqrt_D = math.sqrt(D)
            t1 = (-b + sqrt_D) / (2*a)
            t2 = (-b - sqrt_D) / (2*a)

            # Обработка t1
            if t1 > 0.0:
                roots.extend([math.sqrt(t1), -math.sqrt(t1)])
            elif t1 == 0.0:
                roots.append(0.0)

            # Обработка t2
            if t2 > 0.0:
                root_t2_pos = math.sqrt(t2)
                root_t2_neg = -math.sqrt(t2)
                # Проверяем, чтобы не дублировать корень 0
                if not (t1 == 0.0 and 0.0 in roots):
                    if root_t2_pos != 0.0:
                        roots.append(root_t2_pos)
                    if root_t2_neg != 0.0:
                        roots.append(root_t2_neg)
            elif t2 == 0.0 and 0.0 not in roots:
                roots.append(0.0)

            # Удаляем дубликаты и сортируем
            unique_roots = sorted(set(roots))

            if unique_roots:
                roots_str = ", ".join(f"{r:.4f}" for r in unique_roots)
                return unique_roots, f"Корни уравнения: {roots_str}"
            else:
                return [], "Нет действительных корней"

    @staticmethod
    def solve_from_user_input() -> Tuple[List[float], str]:
        """
        Решение уравнения с запросом коэффициентов у пользователя

        Returns:
            Кортеж (roots, message)
        """
        print("Решение биквадратного уравнения ax^4 + bx^2 + c = 0")

        try:
            a = InputHandler.get_coef(1, "Введите коэффициент A: ")
            b = InputHandler.get_coef(2, "Введите коэффициент B: ")
            c = InputHandler.get_coef(3, "Введите коэффициент C: ")
        except ValueError as e:
            return [], f"Ошибка ввода: {e}"

        return BiquadraticSolver.solve(a, b, c)


def main():
    """Основная функция для запуска из командной строки"""
    roots, message = BiquadraticSolver.solve_from_user_input()
    print(message)

    if roots:
        print(f"Количество корней: {len(roots)}")
        for i, root in enumerate(roots, 1):
            print(f"Корень {i}: {root:.6f}")


if __name__ == "__main__":
    main()
