"""
Симметричная матрица

Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
затем элементы матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести YES, если матрица симметрична относительно главной диагонали, и слово NO в противном случае.
"""
import sys
import os

DEBUG = False
if DEBUG:
    input_filename = 'input.txt'
    if os.path.exists(input_filename):
        sys.stdin = open(input_filename, encoding='utf-8')


def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                print('NO')
                return
    print('YES')


if __name__ == '__main__':
    main()
