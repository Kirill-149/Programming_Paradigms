import json
import sys
import os
from Lab_3.lab_python_fp.field import field
from Lab_3.lab_python_fp.gen_random import gen_random
from Lab_3.lab_python_fp.unique import Unique
from Lab_3.lab_python_fp.print_result import print_result
from Lab_3.lab_python_fp.cm_timer import cm_timer_1


# Путь к файлу с данными
DATA_FILE = "data_light.json"


@print_result
def f1(arg):
    """Вывести отсортированный список профессий без повторений (без учета регистра)"""
    return sorted(set(Unique(field(arg, 'job-name'), ignore_case=True)), key=str.lower)


@print_result
def f2(arg):
    """Фильтровать входной массив и возвращать только те элементы, которые начинаются со слова 'программист'"""
    return list(filter(lambda x: x.lower().startswith('программист'), arg))


@print_result
def f3(arg):
    """Модифицировать каждый элемент массива, добавив строку 'с опытом Python'"""
    return list(map(lambda x: f"{x} с опытом Python", arg))


@print_result
def f4(arg):
    """Сгенерировать для каждой специальности зарплату от 100 000 до 200 000 рублей"""
    salaries = list(gen_random(len(arg), 100000, 200000))
    return [f"{job}, зарплата {salary} руб." for job, salary in zip(arg, salaries)]


if __name__ == '__main__':
    # Проверяем наличие файла с данными
    if not os.path.exists(DATA_FILE):
        print(f"Файл {DATA_FILE} не найден.")
        print("Создаем тестовые данные...")
        # Создаем тестовые данные
        test_data = [
            {"job-name": "Программист Python", "salary": "150000"},
            {"job-name": "Программист Java", "salary": "140000"},
            {"job-name": "Программист C++", "salary": "160000"},
            {"job-name": "Аналитик данных", "salary": "120000"},
            {"job-name": "Программист Python", "salary": "155000"},
            {"job-name": "программист JavaScript", "salary": "135000"},
            {"job-name": "Менеджер проекта", "salary": "110000"}
        ]
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(test_data, f, ensure_ascii=False, indent=2)
        print(f"Тестовые данные сохранены в {DATA_FILE}")
        data = test_data
    else:
        # Загружаем данные из файла
        with open(DATA_FILE, encoding='utf-8') as f:
            data = json.load(f)
        print(f"Данные загружены из {DATA_FILE}")

    print(f"Загружено {len(data)} записей")

    # Выполняем цепочку функций
    with cm_timer_1():
        result = f4(f3(f2(f1(data))))

    print(f"\nИтоговый результат содержит {len(result)} элементов")
