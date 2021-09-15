# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

def reverse_num_2(num):
    #a = 1
    if num <= 1:
        return 1
    else:
        return 1/((-2)**(num-1)) + reverse_num_2(num-1)
        #return 1/(2**(num-1))


def main():
    print(reverse_num_2(1))
    print(reverse_num_2(2))
    print(reverse_num_2(3))
    print(reverse_num_2(4))
    print(reverse_num_2(10))
    print(reverse_num_2(0))
    

if __name__ == '__main__':
    main()
    
