# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

def num_sum_mul(num):
    if num < 100 or num > 999:
        rezult = 'Введите трехзначное число'
    else:
        rezult = f'Число: {num}\nСумма цифр: {int(str(num)[0]) + int(str(num)[1]) + int(str(num)[2])}\nПроизведение:' \
                 f'{int(str(num)[0]) * int(str(num)[1]) * int(str(num)[2])}'
    return rezult


def main():
    print(num_sum_mul(333))
    print(num_sum_mul(12))
    print(num_sum_mul(254))
    print(num_sum_mul(777))


if __name__ == '__main__':
    main()
