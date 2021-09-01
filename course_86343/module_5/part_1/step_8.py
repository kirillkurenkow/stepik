"""
Диагонали параллельные главной

На вход программе подается натуральное число n.
Напишите программу, которая создает матрицу размером n × n и заполняет её по следующему правилу:
* на главной диагонали на месте каждого элемента должно стоять число 0;
* на двух диагоналях, прилегающих к главной, число 1;
* на следующих двух диагоналях число 2, и т.д.

Формат входных данных
На вход программе подается натуральное число nn — количество строк и столбцов в матрице.

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
    matrix = [[0 for _ in range(number)] for _ in range(number)]
    for i in range(number - 1):
        for j in range(1, number):
            try:
                matrix[i+j][i] = matrix[i][i+j] = j
                matrix[i+j][i] = matrix[i][i+j] = j
            except IndexError:
                pass
    print_matrix_with_spaces(matrix)


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
