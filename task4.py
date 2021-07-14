# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random


def get_random(a, b):
    c = 'abcdefghijklmnopqrstuvwxyz'
    if isinstance(a, int) and isinstance(b, int):
        num = random.randint(a, b)
    elif isinstance(a, float) and isinstance(b, float):
        num = f'{random.uniform(a, b):.2f}'
    elif c.find(a.lower()) >= 0 and c.find(b.lower()) >= 0:
        num = c[random.randint(c.find(a.lower()), c.find(b.lower()))]
    else:
        num = 'Введены неверные границы'
    return num


def main():
    print(get_random(1, 258))
    print(get_random(5.8, 7.9))
    print(get_random('a', 'f'))
    print(get_random('t', 'z'))
    print(get_random('A', 'Z'))
    print(get_random('ae', 'tw'))


if __name__ == '__main__':
    main()