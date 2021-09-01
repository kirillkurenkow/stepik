"""
Побочная диагональ

На вход программе подается натуральное число n.
Напишите программу, которая создает матрицу размером n × n и заполняет её по следующему правилу:
* числа на побочной диагонали равны 1;
* числа, стоящие выше этой диагонали, равны 0;
* числа, стоящие ниже этой диагонали, равны 2.

Полученную матрицу выведите на экран. Числа в строке разделяйте одним пробелом.

Формат входных данных
На вход программе подается натуральное число n — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии с условием задачи.

Примечание. Побочная диагональ — это диагональ, идущая из правого верхнего в левый нижний угол матрицы.
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
    matrix = [[... for _ in range(number)] for _ in range(number)]
    for i in range(number):
        matrix[i][number - i - 1] = 1
    for i in range(number):
        for j in range(number):
            if i < number - j - 1:
                matrix[i][j] = 0
            elif i > number - j - 1:
                matrix[i][j] = 2
    [print(*row) for row in matrix]


if __name__ == '__main__':
    main()
