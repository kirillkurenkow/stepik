"""
Треугольник Паскаля 2
На вход программе подается натуральное число n. Напишите программу, которая выводит первые n строк треугольника Паскаля.

Формат входных данных
На вход программе подается число n (n ≥ 1).

Формат выходных данных
Программа должна вывести первые nn строк треугольника Паскаля, каждую на отдельной строке в соответствии с образцом.
"""
import sys
import os

DEBUG = False
if DEBUG:
    input_filename = 'input.txt'
    if os.path.exists(input_filename):
        sys.stdin = open(input_filename, encoding='utf-8')


def main():
    result = [
        [1],
        [1, 1],
    ]
    number = int(input())
    if number < 2:
        [print(*row) for row in result[:number]]
    else:
        for i in range(1, number - 1):
            new_row = [1] + [result[i][j] + result[i][j + 1] for j in range(len(result[i]) - 1)] + [1]
            result.append(new_row)
        [print(*row) for row in result]


if __name__ == '__main__':
    main()
