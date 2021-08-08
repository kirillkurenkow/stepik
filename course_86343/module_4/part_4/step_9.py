"""
Вывести матрицу 2
На вход программе подаются два натуральных числа n и m, каждое на отдельной строке —
количество строк и столбцов в матрице.
Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке;
подряд идут элементы сначала первой строки, затем второй, и т.д.

Напишите программу, которая считывает элементы матрицы один за другим, выводит их в виде матрицы,
выводит пустую строку, и снова ту же матрицу, но уже поменяв местами строки со столбцами:
первая строка выводится как первый столбец, и так далее.

Формат входных данных
На вход программе подаются два числа n и m — количество строк и столбцов в матрице, далее идут n×m слов,
каждое на отдельной строке.

Формат выходных данных
Программа должна вывести считанную матрицу, за ней пустую строку, и ту же матрицу,
но поменяв местами строки со столбцами. Элементы матрицы разделять одним пробелом.
"""
import sys
import os

DEBUG = True
if DEBUG:
    input_filename = 'input.txt'
    if os.path.exists(input_filename):
        sys.stdin = open(input_filename, encoding='utf-8')


def main():
    m, n = (int(input()) for _ in range(2))
    result_1 = [[input() for _ in range(n)] for _ in range(m)]
    result_2 = [[result_1[j][i] for j in range(m)] for i in range(n)]
    [print(*row) for row in result_1]
    print()
    [print(*row) for row in result_2]


if __name__ == '__main__':
    main()
