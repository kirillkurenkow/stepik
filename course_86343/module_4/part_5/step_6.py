"""
Зеркальное отображение

Дана квадратная матрица чисел. Напишите программу,
которая зеркально отображает её элементы относительно горизонтальной оси симметрии.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
затем элементы матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести матрицу в которой зеркально отображены элементы относительно горизонтальной оси симметрии.
"""
import sys
import os

DEBUG = True
if DEBUG:
    input_filename = 'input.txt'
    if os.path.exists(input_filename):
        sys.stdin = open(input_filename, encoding='utf-8')


def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n // 2):
        for j in range(n):
            matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
    [print(*row) for row in matrix]


if __name__ == '__main__':
    main()
