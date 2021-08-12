# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.


import random


def max_negative(arr):
    a = []
    for i in arr:
        if i < 0:
            a.append(i)
    return f'Массив: {arr}\nМаксимальное отрицательное: {max(a)}\nПозиция в массиве: {arr.index(max(a)) + 1}'


def main():
    print(max_negative([-3, -5, 3, 34, -45]))
    print(max_negative([random.randint(-100, 100) for i in range(10)]))


if __name__ == '__main__':
    main()