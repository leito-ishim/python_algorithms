# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.
import numpy

matrix = []
for j in range(4):
    a, b, c, d = (int(i) for i in input('Введите 4 числа: ').split())
    arr = [a, b, c, d]
    arr.append(sum(arr))
    matrix.append(arr)
matrix_1 = numpy.array(matrix)
print(matrix_1)

