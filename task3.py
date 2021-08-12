# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random


def change_max_min(arr):
    a = max(arr)
    arr[arr.index(a)] = min(arr)
    arr[arr.index(min(arr))] = a
    return arr


arr = [random.randint(0, 100) for i in range(10)]
#arr = [1, 2, 3, 4, 5]
print(arr)
print(change_max_min(arr))

arr_1 = [1, 3, 5, 6, 3, 5, 10]
print(arr_1)
print(change_max_min(arr_1))

arr_2 = [125, 152]
print(arr_2)
print(change_max_min(arr_2))

arr_3 = [random.randint(0, 100) for i in range(10)]
print(arr_3)
print(change_max_min(arr_3))