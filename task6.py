# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

def alphabet(num):
    if num > 0 and num < 27:
        result = 'abcdefghijklmnopqrstuvwxyz'[num-1]
    else:
        result = 'Буквы с таким номером нет в алфавите'
    return result


def main():
    print(alphabet(1))
    print(alphabet(4))
    print(alphabet(27))
    print(alphabet(26))


if __name__ == '__main__':
    main()