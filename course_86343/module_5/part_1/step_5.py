"""
Симметричная матрица

Напишите программу проверки симметричности квадратной матрицы относительно побочной диагонали.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы.

Формат выходных данных
Программа должна вывести YES, если матрица симметрична, и слово NO в противном случае.
"""
import sys

DEBUG = False


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def main():
    number = int(input())
    matrix = [list(map(int, input().split())) for _ in range(number)]
    for i in range(number):
        for j in range(number):
            if matrix[i][j] != matrix[number - j - 1][number - i - 1]:
                print('NO')
                return
    print('YES')


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
