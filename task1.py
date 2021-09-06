# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть
# реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
import random

arr = [random.randrange(-100, 100) for i in range(10)]
print(arr)
n = 1
flag = True
while n < len(arr) or flag is True:
    flag = False
    for i in range(len(arr)-n):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
            flag = True
    n += 1
print(arr)