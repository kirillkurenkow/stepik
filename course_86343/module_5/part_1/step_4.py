"""
Снежинка
На вход программе подается нечетное натуральное число n.
Напишите программу, которая создает матрицу размером n × n заполнив её символами ".".
Затем заполните символами "*" среднюю строку и столбец матрицы, главную и побочную диагональ матрицы.
Выведите полученную матрицу на экран, разделяя элементы пробелами.

Формат входных данных
На вход программе подается нечетное натуральное число n, (n > 3) — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии с условием задачи.
"""
import sys
from typing import List, Any

DEBUG = False
T_MATRIX = List[List[Any]]


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def print_matrix_with_spaces(matrix: T_MATRIX) -> None:
    [print(*row) for row in matrix]


def main():
    number = int(input())
    matrix = [['.' for _ in range(number)] for _ in range(number)]
    center = number // 2

    for i in range(number):
        for j in range(number):
            if i == center or j == center or i == j or i == (number - j - 1):
                matrix[i][j] = '*'

    print_matrix_with_spaces(matrix)


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
