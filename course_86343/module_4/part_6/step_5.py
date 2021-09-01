"""
Заполнение 3

На вход программе подается натуральное число n.
Напишите программу, которая создает матрицу размером n × n заполнив её в соответствии с образцом.

Формат входных данных
На вход программе подается натуральное число n — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом: р
азместить единицы на главной и побочной диагоналях, остальные позиции матрицы заполнить нулями.

Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 3 символа на каждый элемент.
Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение.
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
    matrix = [[0 for _ in range(number)] for _ in range(number)]
    for i in range(number):
        for j in range(number):
            if i == j or i == number - j - 1:
                matrix[i][j] = 1
    [print(*row) for row in matrix]


if __name__ == '__main__':
    main()
