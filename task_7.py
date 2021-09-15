# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел
# выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.


def check_num(n):
    total = 0
    for i in range(1, n+1):
        total += i
        if total != (i*(i+1)/2):
            return f'Для числа {i} равенство (1+2+...+n = n(n+1)/2) не выполняется'
        #print(i)
    return f'Для всех чисел из диапазона от 0 до {n} равенство (1+2+...+n = n(n+1)/2) выполняется'


def main():
    print(check_num(10000000))


if __name__ == '__main__':
    main()
    