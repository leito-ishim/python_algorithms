# 1. Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
import timeit


def count_num(succession, num):
    return str(succession).count(str(num))


def count_num_2(succession, num):
    count = 0
    for i in str(succession):
        if i == str(num):
            count += 1
    return count


#print(count_num_2(34363452564234434364633563246, 2))
#print(count_num(34363452564234434364633563246, 2))

print(timeit.timeit('count_num(34363452564234434364633563246, 2)', globals=globals())) # 0.902369338
print(timeit.repeat('count_num(34363452564234434364633563246, 2)', globals=globals()))
t = timeit.Timer('count_num(34363452564234434364633563246, 2)', globals=globals())
print(t.timeit())

print(timeit.timeit('count_num_2(34363452564234434364633563246, 2)', setup='from __main__ import count_num_2'))
# 8.716867017999999

# Первый вариант, без использования цикла for в десять раз быстрее.