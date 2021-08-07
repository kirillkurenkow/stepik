"""
Список по образцу 2
На вход программе подается число n. Напишите программу, которая создает и выводит построчно вложенный список,
состоящий из nn списков [[1], [1, 2], [1, 2, 3], ..., [1, 2, ..., n]].

Формат входных данных
На вход программе подается натуральное число n.

Формат выходных данных
Программа должна вывести построчно указанный вложенный список.
"""
import sys
import os

DEBUG = True
if DEBUG:
    input_filename = 'input.txt'
    if os.path.exists(input_filename):
        sys.stdin = open(input_filename, encoding='utf-8')


def main():
    number = int(input())
    result = list()
    for i in range(number):
        result.append(list(range(1, i + 2)))
    print(*result, sep='\n')


if __name__ == '__main__':
    main()
