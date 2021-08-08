"""
Обмен столбцов

Напишите программу, которая меняет местами столбцы в матрице.

Формат входных данных
На вход программе на разных строках подаются два натуральных числа n и m — количество строк и столбцов в матрице,
затем элементы матрицы построчно через пробел, затем числа i и j — номера столбцов, подлежащих обмену.

Формат выходных данных
Программа должна вывести указанную таблицу с замененными столбцами.
"""
import sys
import os

DEBUG = True
if DEBUG:
    input_filename = 'input.txt'
    if os.path.exists(input_filename):
        sys.stdin = open(input_filename, encoding='utf-8')


def main():
    n, m = map(int, (input() for _ in range(2)))
    matrix = [list(map(int, input().split())) for _ in range(n)]
    i, j = map(int, input().split())
    for k in range(n):
        matrix[k][i], matrix[k][j] = matrix[k][j], matrix[k][i]
    [print(*row) for row in matrix]


if __name__ == '__main__':
    main()
