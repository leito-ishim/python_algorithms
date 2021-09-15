#9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

def search_max(*args):
    total = []
    for i in args:
        summa = 0
        for j in str(i):
            summa += int(j)
        total.append(summa)
    return f'Наибольшее число по сумме цифр: {args[total.index(max(total))]}, сумма цифр: {max(total)}'


def main():
    print(search_max(345, 111, 11, 10000000, 123))
    print(search_max(45345, 453, 2346, 9999999999, 44, 4343535, 3))
    print(search_max(1, 2, 3, 4))
    

if __name__ == '__main__':
    main()
    
