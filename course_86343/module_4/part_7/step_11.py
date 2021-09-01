"""
Возведение матрицы в степень 🌶️

Напишите программу, которая возводит квадратную матрицу в m-ую степень.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
затем элементы матрицы, затем натуральное число m.

Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.
"""
import sys
from typing import List, Any

DEBUG = False
T_MATRIX = List[List[Any]]


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def multiply_matrices(matrix_1: T_MATRIX, matrix_2: T_MATRIX) -> T_MATRIX:
    result = [[... for _ in range(len(matrix_2[0]))] for _ in matrix_1]
    for i in range(len(matrix_1)):
        for j in range(len(matrix_2[0])):
            sum_ = 0
            for element_1, element_2 in zip(matrix_1[i], [row[j] for row in matrix_2]):
                sum_ += element_1 * element_2
            result[i][j] = sum_
    return result


def print_matrix_with_spaces(matrix: T_MATRIX) -> None:
    [print(*row) for row in matrix]


def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    m = int(input())
    result = matrix.copy()
    for _ in range(m - 1):
        result = multiply_matrices(matrix, result)
    print_matrix_with_spaces(result)


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
