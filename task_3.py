# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

def reverse_num(num):
    if len(str(num)) <= 1:
        return str(num)
    else:
        return str(num)[len(str(num))-1] + reverse_num(int(str(num)[:-1]))
       
        


def main():
    print(reverse_num(12345))
    print(reverse_num(3))
    print(reverse_num(43636356))
    print(reverse_num(2353))
    

if __name__ == '__main__':
    main()

