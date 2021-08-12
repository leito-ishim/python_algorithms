# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

# Вариант 1
def two_min(arr):
    min_1 = min(arr)
    arr.remove(min_1)
    min_2 = min(arr.remove(min_1))
    return f'Два минимальных элемнта массива {arr}: {min_1, min_2}'

# Вариант 2


def two_min_2(arr):
    return f'Два минимальных элемнта массива {arr}: {sorted(arr)[0], sorted(arr)[1]}'


def main():
    print(two_min([5, 4, 1, 7, 2, 8]))
    print(two_min([5, 4, 1, 7, 2, 1]))
    print(two_min_2([5, 4, 1, 7, 2, 8]))
    print(two_min_2([5, 4, 1, 7, 2, 1]))


if __name__ == '__main__':
    main()

