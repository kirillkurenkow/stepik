"""
Список по образцу 1
На вход программе подается число n.
Напишите программу, которая создает и выводит построчно вложенный список,
состоящий из n списков [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].

Формат входных данных
На вход программе подается натуральное число n.

Формат выходных данных
Программа должна вывести построчно указанный вложенный список.
"""
import sys
import os

DEBUG = True
if DEBUG:
    filename = 'input.txt'
    if os.path.exists(filename):
        sys.stdin = open(filename, encoding='utf-8')


def main():
    number = int(input())
    result = [list(range(1, number + 1)) for _ in range(number)]
    print(*result, sep='\n')


if __name__ == '__main__':
    main()
