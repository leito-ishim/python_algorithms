# 1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
# состоящая только из маленьких латинских букв.Требуется найти количество различных подстрок в этой строке.
import hashlib

def kabin_karp_count(s, t):
    count = 0
    len_sub = len(t)
    h_subs = hashlib.sha1(t.encode('utf-8')).hexdigest()
    for i in range(len(s) - len_sub +1):
        if h_subs == hashlib.sha1(s[i:i+len_sub].encode('utf-8')).hexdigest():
            count += 1
    
    return f'В строке: {s}\nподстрока: >{t}< встречается {count} раз.'



def main():
    print(kabin_karp_count('aaaassssmdvebbvvkjdbvbshsnsbvsnslsvefbfheoeuvhyefvdgebgjghjjdb', 'b'))
    print(kabin_karp_count('aabbaaccffrreedd', 'aa'))
    print(kabin_karp_count('aabbaaccffrreedd', 'a'))
    print(kabin_karp_count('aabbaaccffrreedd', 'aаа'))
    print(kabin_karp_count('aabbaaccffsahgawwiguwgbyugwihgueagihguaregisgsghergirwrreedd', 'a'))


if __name__ == '__main__':
    main()