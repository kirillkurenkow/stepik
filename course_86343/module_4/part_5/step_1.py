"""
Таблица умножения

На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрице.
Создайте матрицу mult размером n × m и заполните её таблицей умножения по формуле mult[i][j] = i * j.

Формат входных данных
На вход программе на разных строках подаются два числа n и m — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести таблицу умножения отводя на вывод каждого числа ровно 3 символа
(для этого используйте строковый метод ljust()).
"""
import sys
import os

DEBUG = True
if DEBUG:
    input_filename = 'input.txt'
    if os.path.exists(input_filename):
        sys.stdin = open(input_filename, encoding='utf-8')


def main():
    n, m = map(int, (input() for _ in range(2)))
    table = ((i * j for j in range(m)) for i in range(n))
    for row in table:
        for element in row:
            print(str(element).ljust(3), end='')
        print()


if __name__ == '__main__':
    main()
