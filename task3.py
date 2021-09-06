# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся
# элементы, которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки
# исходного массива. Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
import random

def median_arr(arr):
    arr_copy = arr.copy()
    for i in range(len(arr_copy)//2):
        arr_copy.remove(max(arr_copy))
        arr_copy.remove(min(arr_copy))
    return arr_copy[0]
        

arr = [random.randint(0, 100) for i in range(2 * random.randint(1, 10) + 1)]
print(arr)
#print(sorted(arr))
print(median_arr(arr))


