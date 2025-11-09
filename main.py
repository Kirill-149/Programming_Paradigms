import sys
import math

def get_coef(index, prompt):
    try:
        coef_str = sys.argv[index]
    except:
        print(prompt)
        coef_str = input()
    coef = float(coef_str)
    return coef

def main():
    a = get_coef(1, "Введите A: ")
    b = get_coef(2, "Введите B: ")
    c = get_coef(3, "Введите C: ")

    D = b*b - 4*a*c

    if D < 0.0:
        print("Нет корней (дискриминант отрицательный)")
    elif D == 0.0:
        t0 = -b / (2*a)
        if t0 > 0.0:
            print("Корень уравнения:", math.sqrt(t0))
            print("Корень уравнения:", -math.sqrt(t0))
        elif t0 == 0.0:
            print("Корень уравнения: 0")
        else:
            print("Нет действительных корней")
    else:
        t1 = (-b + math.sqrt(D)) / (2*a)
        if t1 > 0.0:
            print("Корень уравнения:", math.sqrt(t1))
            print("Корень уравнения:", -math.sqrt(t1))
        elif t1 == 0.0:
            print("Корень уравнения: 0")

        t2 = (-b - math.sqrt(D)) / (2*a)
        if t2 > 0.0:
            print("Корень уравнения:", math.sqrt(t2))
            print("Корень уравнения:", -math.sqrt(t2))
        elif t2 == 0.0:
            print("Корень уравнения: 0")

        if t1 < 0.0 and t2 < 0.0:
            print("Нет действительных корней")

if __name__ == "__main__":
    main()
