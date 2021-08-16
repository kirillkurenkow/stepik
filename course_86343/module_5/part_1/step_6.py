"""
Латинский квадрат 🌶️

Латинским квадратом порядка nn называется квадратная матрица размером n × n,
каждая строка и каждый столбец которой содержат все числа от 1 до n.
Напишите программу, которая проверяет, является ли заданная квадратная матрица латинским квадратом.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
затем элементы матрицы: n строк, по n чисел в каждой, разделённые пробелами.

Формат выходных данных
Программа должна вывести слово YES, если матрица является латинским квадратом, и слово NO, если не является.
"""
import sys

DEBUG = True


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def main():
    number = int(input())
    matrix = [list(map(int, input().split())) for _ in range(number)]
    sample = set(range(1, number + 1))
    for i in range(number):
        if set(matrix[i]) != sample or set(matrix[j][i] for j in range(number)) != sample:
            print('NO')
            return
    print('YES')


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
