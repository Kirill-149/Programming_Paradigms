# features/steps/biquadratic_steps.py
import sys
import os
import math

# Добавляем путь к корню проекта ДО импорта behave
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, project_root)

print(f"Project root added to path: {project_root}")

# Теперь импортируем behave
from behave import given, when, then

# Импортируем наш модуль
try:
    from equation_solver.biquadratic import BiquadraticSolver
    print("Successfully imported BiquadraticSolver")
except ImportError as e:
    print(f"Import error: {e}")
    print(f"Current sys.path: {sys.path}")
    raise


@given('биквадратное уравнение с коэффициентами A={a:g}, B={b:g}, C={c:g}')
def step_given_biquadratic_equation(context, a, b, c):
    """Установка коэффициентов биквадратного уравнения"""
    print(f"Step: биквадратное уравнение с коэффициентами A={a}, B={b}, C={c}")
    context.a = float(a)
    context.b = float(b)
    context.c = float(c)


@given('коэффициент A равен 0')
def step_given_a_is_zero(context):
    """Установка нулевого коэффициента A"""
    print("Step: коэффициент A равен 0")
    context.a = 0.0
    context.b = 1.0
    context.c = 1.0


@given('коэффициенты являются числами')
def step_given_coefficients_are_numbers(context):
    """Проверка что коэффициенты - числа"""
    print("Step: коэффициенты являются числами")
    context.a = 1.0
    context.b = 2.0
    context.c = 3.0


@when('я решаю биквадратное уравнение')
def step_when_solve_biquadratic(context):
    """Решение биквадратного уравнения"""
    print(f"Step: решаю уравнение с A={context.a}, B={context.b}, C={context.c}")
    context.roots, context.message = BiquadraticSolver.solve(context.a, context.b, context.c)
    print(f"Result: roots={context.roots}, message='{context.message}'")


@when('я проверяю валидность коэффициентов')
def step_when_validate_coefficients(context):
    """Проверка валидности коэффициентов"""
    print(f"Step: проверяю валидность коэффициентов A={context.a}, B={context.b}, C={context.c}")
    context.is_valid, context.error_message = BiquadraticSolver.validate_coefficients(
        context.a, context.b, context.c
    )
    print(f"Validation result: is_valid={context.is_valid}, error='{context.error_message}'")


@then('уравнение должно иметь {count:d} действительных корней')
def step_then_equation_has_roots(context, count):
    """Проверка количества корней"""
    print(f"Step: проверяю что уравнение имеет {count} корней, actual={len(context.roots)}")
    assert len(context.roots) == count, f"Ожидалось {count} корней, но получено {len(context.roots)}"


@then('корни должны быть {roots}')
def step_then_roots_should_be(context, roots):
    """Проверка конкретных значений корней"""
    print(f"Step: проверяю что корни равны {roots}")
    expected_roots = [float(r.strip()) for r in roots.split(',')]
    assert len(context.roots) == len(expected_roots)

    # Сортируем для сравнения
    sorted_expected = sorted(expected_roots)
    sorted_actual = sorted(context.roots)

    for expected, actual in zip(sorted_expected, sorted_actual):
        assert math.isclose(actual, expected, rel_tol=1e-9), f"Ожидался корень {expected}, но получен {actual}"


@then('уравнение не должно иметь действительных корней')
def step_then_no_real_roots(context):
    """Проверка отсутствия действительных корней"""
    print(f"Step: проверяю отсутствие корней, actual={len(context.roots)}")
    assert len(context.roots) == 0, f"Ожидалось 0 корней, но получено {len(context.roots)}"


@then('сообщение должно содержать "{text}"')
def step_then_message_contains(context, text):
    """Проверка текста сообщения"""
    print(f"Step: проверяю что сообщение содержит '{text}'")
    print(f"Actual message: '{context.message}'")
    assert text in context.message, f"Сообщение '{context.message}' не содержит '{text}'"


@then('коэффициенты должны быть признаны невалидными')
def step_then_coefficients_invalid(context):
    """Проверка что коэффициенты невалидны"""
    print(f"Step: проверяю что коэффициенты невалидны, actual={context.is_valid}")
    assert not context.is_valid, "Коэффициенты должны быть невалидными"


@then('коэффициенты должны быть признаны валидными')
def step_then_coefficients_valid(context):
    """Проверка что коэффициенты валидны"""
    print(f"Step: проверяю что коэффициенты валидны, actual={context.is_valid}")
    assert context.is_valid, "Коэффициенты должны быть валидными"


@then('сообщение об ошибке должно быть "{error}"')
def step_then_error_message(context, error):
    """Проверка сообщения об ошибке"""
    print(f"Step: проверяю сообщение об ошибке '{error}'")
    print(f"Actual error: '{context.error_message}'")
    assert context.error_message == error, f"Ожидалась ошибка '{error}', но получена '{context.error_message}'"


@then('корень {index:d} должен быть приблизительно равен {value:g}')
def step_then_root_approximately_equal(context, index, value):
    """Проверка приблизительного значения корня"""
    print(f"Step: проверяю корень {index} ≈ {value}")
    assert 1 <= index <= len(context.roots), f"Нет корня с индексом {index}"
    root = context.roots[index - 1]
    print(f"Actual root[{index}]: {root}")
    assert math.isclose(root, value, rel_tol=1e-9), f"Корень {index}: ожидалось {value}, получено {root}"
