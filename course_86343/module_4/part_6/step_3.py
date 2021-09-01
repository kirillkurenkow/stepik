"""
Заполнение 1

На вход программе подаются два натуральных числа n и m.
Напишите программу, которая создает матрицу размером n × m и заполняет её числами от 1 до n*m в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии с образцом.

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
    n, m = map(int, input().split())
    counter = 1
    result = list()
    for _ in range(n):
        row = list()
        for _ in range(m):
            row.append(str(counter).ljust(3))
            counter += 1
        result.append(row)
    [print(*row) for row in result]


if __name__ == '__main__':
    main()
