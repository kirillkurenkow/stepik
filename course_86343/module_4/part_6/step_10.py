"""
Заполнение спиралью

На вход программе подаются два натуральных числа n и m.
Напишите программу, которая создает матрицу размером n × m заполнив её "спиралью" в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии образцом.

Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 3 символа на каждый элемент.
Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение.
"""
import sys
from typing import List, Any

DEBUG = True
T_MATRIX = List[List[Any]]


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def print_matrix_with_spaces(matrix: T_MATRIX) -> None:
    [print(*row) for row in matrix]


class Counter:
    def __init__(self, max_value: int):
        self.max_value = max_value
        self.value = 1

    def __add__(self, other):
        if self.value + other > self.max_value:
            raise StopIteration
        self.value += other
        return self

    def __le__(self, other):
        return self.value <= other

    def __int__(self):
        return self.value


def main():
    column_size, row_size = map(int, input().split())
    matrix = [[0 for _ in range(row_size)] for _ in range(column_size)]
    counter = Counter(column_size * row_size)
    iteration = 0
    try:
        while counter <= column_size * row_size:
            for i in range(iteration, row_size - iteration):
                matrix[iteration][i] = int(counter)
                counter += 1
            for i in range(iteration + 1, column_size - iteration):
                matrix[i][row_size - iteration - 1] = int(counter)
                counter += 1
            for i in range(row_size - iteration - 2, iteration - 1, -1):
                matrix[column_size - iteration - 1][i] = int(counter)
                counter += 1
            for i in range(column_size - iteration - 2, iteration, -1):
                matrix[i][iteration] = int(counter)
                counter += 1
            iteration += 1
    except StopIteration:
        pass
    print_matrix_with_spaces(matrix)


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
