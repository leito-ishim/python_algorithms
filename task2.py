# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.
import cProfile
import math


# Вариант 1: Обычный способ нахождения простого числа
def prime_num(num):
    lst = []
    for i in range(2, num + 1):
        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)
    return sorted(set(lst))


# Вариант 2: Доработанный с помощью интернета способ нахождения простого числа
def prime_num_v2(num):
    lst = []
    for i in range(2, num + 1):
        for j in lst:
            if j > int((math.sqrt(i)) + 1):
                lst.append(i)
                break
            if i % j == 0:
                break
        else:
            lst.append(i)
    return sorted(set(lst))


# Вариант 3: Нахождение через Решето Эратосфена
def prime_num_eratosfen(num):
    a = [i for i in range(num + 1)]
    a[1] = 0
    lst = []
    i = 2
    while i <= num:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, num + 1, i):
                a[j] = 0
        i += 1
    return lst

def main():
    prime_num(100000)
    prime_num_v2(100000)
    prime_num_eratosfen(100000)


#main()
cProfile.run('main()')

# Вывод: Второй вариант выполняется почти в 10 раз быстрее чем первый, а третий вариант (через решето Эратосфена)
# ускоряет еше в 2 раза