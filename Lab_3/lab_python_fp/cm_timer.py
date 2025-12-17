# lab_python_fp/cm_timer.py
import time
from contextlib import contextmanager


# Способ 1: на основе класса
class cm_timer_1:
    """
    Контекстный менеджер на основе класса для измерения времени выполнения блока кода.
    """
    def __enter__(self):
        self.start_time = time.perf_counter()  # Используем perf_counter для большей точности
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.perf_counter()
        self.elapsed_time = self.end_time - self.start_time
        print(f"time: {self.elapsed_time:.1f}")


# Способ 2: с использованием contextlib
@contextmanager
def cm_timer_2():
    """
    Контекстный менеджер с использованием contextlib для измерения времени выполнения блока кода.
    """
    start_time = time.perf_counter()
    try:
        yield
    finally:
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"time: {elapsed_time:.1f}")


# Пример из задания
if __name__ == '__main__':
    from time import sleep

    print("Пример из задания:")
    print("with cm_timer_1():")
    print("    sleep(5.5)")

    print("\nПример 1: cm_timer_1 с sleep(1.5)")
    with cm_timer_1():
        sleep(1.5)

    print("\nПример 2: cm_timer_2 с sleep(0.7)")
    with cm_timer_2():
        sleep(0.7)
