# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.


def max_min_element(arr):
    max_ = arr.index(max(arr))
    min_ = arr.index(min(arr))
    return sum(arr[min_ + 1: max_]) if max_ > min_ else sum(arr[max_ + 1: min_])


def main():
    print(max_min_element([3, 1, 5, 7, 10]))
    print(max_min_element([1, 5, 2, 2, 2]))


if __name__ == '__main__':
    main()