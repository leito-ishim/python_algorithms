# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        result = 'високосный'
    else:
        result = 'не високосный'
    return f'{year} год - {result}'


def main():
    print(leap_year(2020))
    print(leap_year(1900))
    print(leap_year(2021))


if __name__ == '__main__':
    main()
