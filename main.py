from Lab_2.rectangle import Rectangle
from Lab_2.circle import Circle
from Lab_2.square import Square
import requests

def main():
    N = 4

    # Создание объектов
    rectangle = Rectangle(N, N, "синего")
    circle = Circle(N, "зеленого")
    square = Square(N, "красного")

    # Вывод информации о фигурах
    print(rectangle)
    print(circle)
    print(square)

    # Демонстрация работы внешнего пакета
    print("\n--- Демонстрация работы пакета requests ---")
    try:
        response = requests.get('https://httpbin.org/get')
        print(f"Статус запроса: {response.status_code}")
        print("Запрос выполнен успешно!")
    except Exception as e:
        print(f"Ошибка при выполнении запроса: {e}")

if __name__ == "__main__":
    main()
