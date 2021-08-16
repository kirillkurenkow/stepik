"""
Максимальный в области 2

Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.

[ * * * * x ]
[ * * * x x ]
[ * * x x x ]
[ * x x x x ]
[ x x x x x ]

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы.

Формат выходных данных
Программа должна вывести одно число — максимальный элемент в заштрихованной области квадратной матрицы.
"""
import sys

DEBUG = True


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def main():
    number = int(input())
    matrix = [list(map(int, input().split())) for _ in range(number)]
    shaded_numbers = [x for i, row in enumerate(matrix) for j, x in enumerate(row) if i >= number - 1 - j]
    print(max(shaded_numbers))


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
