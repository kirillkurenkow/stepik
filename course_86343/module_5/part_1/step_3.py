"""
Транспонирование матрицы

Напишите программу, которая транспонирует квадратную матрицу.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы.

Формат выходных данных
Программа должна вывести транспонированную матрицу.

Примечание 1. Транспонированная матрица — матрица, полученная из исходной матрицы заменой строк на столбцы.

Примечание 2. Задачу можно решить без использования вспомогательного списка.
"""
import sys
from typing import Any, List

DEBUG = True
T_MATRIX = List[List[Any]]


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def print_matrix_with_spaces(matrix: T_MATRIX) -> None:
    [print(*row) for row in matrix]


def main():
    number = int(input())
    matrix = [list(map(int, input().split())) for _ in range(number)]
    new_matrix = [[matrix[i][j] for i in range(number)] for j in range(number)]
    print_matrix_with_spaces(new_matrix)


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
