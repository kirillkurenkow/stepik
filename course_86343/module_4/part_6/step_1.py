"""
Шахматная доска

На вход программе подаются два натуральных числа n и m.
Напишите программу для создания матрицы размером n × m, заполнив её символами . и * в шахматном порядке.
В левом верхнем углу должна стоять точка. Выведите полученную матрицу на экран, разделяя элементы пробелами.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу, описанную в условии задачи.
"""
import sys
import os

DEBUG = True
if DEBUG:
    input_filename = 'input.txt'
    if os.path.exists(input_filename):
        sys.stdin = open(input_filename, encoding='utf-8')


def main():
    n, m = map(int, input().split())
    chars = ['.', '*']
    matrix = [[chars[(i + j) % 2] for j in range(m)] for i in range(n)]
    [print(*row) for row in matrix]


if __name__ == '__main__':
    main()
