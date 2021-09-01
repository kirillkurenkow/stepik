"""
Поворот матрицы
Напишите программу, которая поворачивает квадратную матрицу чисел на 90 градусов по часовой стрелке.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
затем элементы матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести результат на экран, числа должны быть разделены одним пробелом.
"""
import sys
import os
from typing import List

DEBUG = False
if DEBUG:
    input_filename = 'input.txt'
    if os.path.exists(input_filename):
        sys.stdin = open(input_filename, encoding='utf-8')


def turn_matrix_90(matrix: List[List]) -> List[List]:
    """
    Turns matrix 90 degrees clockwise

    :param matrix: Square matrix
    :return: New turned matrix
    """
    n = len(matrix[0])
    result = [[matrix[n - j - 1][i] for j in range(n)] for i in range(n)]
    return result


def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    matrix_90 = turn_matrix_90(matrix)
    [print(*row) for row in matrix_90]


if __name__ == '__main__':
    main()
