"""
Заполнение диагоналями 🌶️

На вход программе подаются два натуральных числа n и m.
Напишите программу, которая создает матрицу размером n × m заполнив её "диагоналями" в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом.

Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 3 символа на каждый элемент.
Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇
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


def main():
    n, m = map(int, input().split())
    matrix = [[... for _ in range(m)] for _ in range(n)]
    counter = 1
    for i in range(m + n):
        if i < m:
            matrix[0][i] = counter
            counter += 1
        for j in range(1, n):
            if m > i - j >= 0:
                matrix[j][i-j] = counter
                counter += 1
    print_matrix_with_spaces(matrix)


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
