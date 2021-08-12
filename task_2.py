# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def count_num(num):
    even_count = 0
    odd_count = 0
    for i in str(num):
        if int(i) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return f'В числе {num} четных цифр: {even_count}, нечетных: {odd_count}'



def main():
    print(count_num(3552))
    print(count_num(357655))
    print(count_num(1234567876))
    print(count_num(0))


if __name__ == '__main__':
    main()


