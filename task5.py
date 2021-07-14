# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

def letter_in_alphabet(a, b):
    c = 'abcdefghijklmnopqrstuvwxyz'
    num = abs(c.find(a.lower()) - c.find(b.lower())) - 1 if a.lower() != b.lower() \
        else abs(c.find(a.lower()) - c.find(b.lower()))
    return f'Буква "{a}" в алфавите под номером: {c.find(a.lower()) + 1}, буква "{b}" под номером: ' \
           f'{c.find(b.lower()) + 1}, количество букв между ними: {num}'


def main():
    print(letter_in_alphabet('a', 'z'))
    print(letter_in_alphabet('a', 'b'))
    print(letter_in_alphabet('z', 'b'))
    print(letter_in_alphabet('A', 'a'))


if __name__ == '__main__':
    main()