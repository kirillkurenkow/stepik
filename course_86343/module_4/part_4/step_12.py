"""
Максимальный в области 1

Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.

[ X         ]
[ X X       ]
[ X X X     ]
[ X X X X   ]
[ X X X X X ]

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
затем элементы матрицы (целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести одно число — максимальный элемент в заштрихованной области квадратной матрицы.

Примечание. Элементы главной диагонали также учитываются.
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
    if DEBUG:
        print(*matrix, sep='\n')
    result = []
    for i in range(number):
        for j in range(i + 1):
            result.append(matrix[i][j])
    if DEBUG:
        print(result)
    print(max(result))


if __name__ == '__main__':
    main()
