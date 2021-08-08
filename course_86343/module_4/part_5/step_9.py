"""
Магический квадрат

Магическим квадратом порядка n называется квадратная таблица размера n × n,
составленная из всех чисел 1, 2, 3, ..., n^2 так, что суммы по каждому столбцу,
каждой строке и каждой из двух диагоналей равны между собой.
Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
затем элементы матрицы: n строк, по n чисел в каждой, разделённые пробелами.

Формат выходных данных
Программа должна вывести слово YES, если матрица является магическим квадратом, и слово NO в противном случае.
"""
import sys
import os

DEBUG = True
if DEBUG:
    input_filename = 'input.txt'
    if os.path.exists(input_filename):
        sys.stdin = open(input_filename, encoding='utf-8')


def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    row_sums = [sum(row) for row in matrix]
    column_sums = [sum((matrix[j][i] for j in range(n))) for i in range(n)]
    diagonal_sums = [sum((matrix[i][i] for i in range(n))), sum((matrix[n - i - 1][n - i - 1] for i in range(n)))]
    numbers = row_sums + column_sums + diagonal_sums
    all_numbers_present = set(range(1, n**2 + 1)) == set([element for row in matrix for element in row])
    print('YES' if (len(set(numbers)) == 1) and all_numbers_present else 'NO')


if __name__ == '__main__':
    main()
