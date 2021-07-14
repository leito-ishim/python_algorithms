# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

def average(a, b, c):
    if (b > a > c) or (b < a < c):
        result = f'среднее {a}'
    elif (a > b > c) or (a < b < c):
        result = f'среднее {b}'
    elif (a > c > b) or (a < c < b):
        result = f'среднее {c}'
    else:
        result = 'среднего числа нет'
    return f'Среди чисел {a, b, c} {result}'


def main():
    print(average(4, 5, 6))
    print(average(10, 100000, 10554))
    print(average(0, 0, 0))


if __name__ == '__main__':
    main()