# 4. Определить, какое число в массиве встречается чаще всего.

import random


def max_repetition(arr):
    a = max(zip((arr.count(i) for i in set(arr)), set(arr)))
    return f'В массиве {arr} чаще всего встречается элемент {a[1]}, всего: {a[0]} раз'


def main():
    print(max_repetition([random.randint(1, 10) for i in range(30)]))
    print(max_repetition([1, 1, 1, 1, 1, 1, 2, 3, 4, 3, 4, 3, 4, 3]))


if __name__ == '__main__':
    main()