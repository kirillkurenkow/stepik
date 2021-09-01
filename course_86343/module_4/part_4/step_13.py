"""
Максимальный в области 2
Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.

[ X       X ]
[ X X   X X ]
[ X X X X X ]
[ X X   X X ]
[ X       X ]

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
затем элементы матрицы (целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести одно число — максимальный элемент в заштрихованной области квадратной матрицы.
"""
import sys
import os

DEBUG = False
if DEBUG:
    input_filename = 'input.txt'
    if os.path.exists(input_filename):
        sys.stdin = open(input_filename, encoding='utf-8')


def main():
    number = int(input())
    matrix = [list(map(int, input().split())) for _ in range(number)]
    result = []
    for i in range(number):
        for j in range(number):
            if j <= i <= number - 1 - j:
                result.append(matrix[i][j])
            elif j >= i >= number - 1 - j:
                result.append(matrix[i][j])
    if DEBUG:
        print(result)
    print(max(result))


if __name__ == '__main__':
    main()
