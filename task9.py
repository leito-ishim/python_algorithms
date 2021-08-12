# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

def max_elem_matrix(arr):
    max_arr = []
    for i in range(len(arr[0])):
        min_arr = []
        for j in range(len(arr)):
            min_arr.append(arr[j][i])
        max_arr.append(min(min_arr))
    return max(max_arr)


def main():
    print(max_elem_matrix([[1, 1, 1, 2], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]))


if __name__ == '__main__':
    main()