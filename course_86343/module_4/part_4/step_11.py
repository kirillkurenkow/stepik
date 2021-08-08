"""
Больше среднего

Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке,
больших среднего арифметического элементов данной строки.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
затем элементы матрицы (целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести n чисел — для каждой строки количество элементов матрицы,
больших среднего арифметического элементов данной строки.
"""
import sys
import os

DEBUG = True
if DEBUG:
    input_filename = 'input.txt'
    if os.path.exists(input_filename):
        sys.stdin = open(input_filename, encoding='utf-8')


def main():
    number = int(input())
    matrix = [[int(x) for x in input().split()] for _ in range(number)]
    result = [len([x for x in row if x > sum(row) / len(row)]) for row in matrix]
    print(*result, sep='\n')


if __name__ == '__main__':
    main()
