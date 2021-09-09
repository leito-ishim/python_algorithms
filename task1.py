# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# в рамках первых трех уроков. Проанализировать результат и определить программы с
# наиболее эффективным использованием памяти.

# В решениях предыдущих заданий все переменные находятся в функциях, оценивать их сложно, поэтому просто поработал
# с функцией getsizeof()
import sys
# from decimal import Decimal

print(sys.getsizeof(5))     # 28
print(sys.getsizeof(-5))     # 28
print(sys.getsizeof(1000000))     # 28
print(sys.getsizeof(-1000000000000))     # 32
print(sys.getsizeof(-1000000000000000000000))     # 36

print(sys.getsizeof(5.3))   # 24
print(sys.getsizeof(11111.22222))   # 24
print(sys.getsizeof(Decimal(5.0)))      # 104

print(sys.getsizeof(True))  # 28
print(sys.getsizeof(False))  # 24

print(sys.getsizeof(f''))               # 49
print(sys.getsizeof(f'H'))              # 50
print(sys.getsizeof(f'He'))             # 51
print(sys.getsizeof(f'Hel'))             # 52 Каждая буква добавляет 1 байт
print(sys.getsizeof('Hello world'))     # 60
print(sys.getsizeof([1, 2, 3, 4]))      # 88
print(sys.getsizeof([2, 2]))            # 72
print(sys.getsizeof((2, 2)))            # 56




