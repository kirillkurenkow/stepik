"""
Сложение матриц

Напишите программу для вычисления суммы двух матриц.

Формат входных данных
На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрицах,
затем элементы первой матрицы, затем пустая строка, далее следуют элементы второй матрицы.

Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.
"""
import sys
import os
from typing import Any, List

# Debug
DEBUG = True
if DEBUG:
    input_filename = 'input.txt'
    if os.path.exists(input_filename):
        sys.stdin = open(input_filename, encoding='utf-8')

# Types
T_MATRIX = List[List[Any]]


def add_matrices(matrix_1: T_MATRIX, matrix_2: T_MATRIX) -> T_MATRIX:
    result = [[... for _ in range(len(matrix_1[0]))] for _ in range(len(matrix_1))]
    for i, (row_1, row_2) in enumerate(zip(matrix_1, matrix_2)):
        for j, (element_1, element_2) in enumerate(zip(row_1, row_2)):
            result[i][j] = element_1 + element_2
    return result


def print_matrix_with_spaces(matrix: T_MATRIX) -> None:
    [print(*row) for row in matrix]


def main():
    n, m = map(int, input().split())
    matrix_1 = [list(map(int, input().split())) for _ in range(n)]
    input()
    matrix_2 = [list(map(int, input().split())) for _ in range(n)]
    result_matrix = add_matrices(matrix_1, matrix_2)
    print_matrix_with_spaces(result_matrix)


if __name__ == '__main__':
    main()
