"""
Упаковка дубликатов
На вход программе подается строка текста, содержащая символы. Напишите программу,
которая упаковывает последовательности одинаковых символов заданной строки в подсписки.

Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела.

Формат выходных данных
Программа должна вывести указанный вложенный список.
"""
import sys
import os

DEBUG = False
if DEBUG:
    input_filename = 'input.txt'
    if os.path.exists(input_filename):
        sys.stdin = open(input_filename, encoding='utf-8')


def main():
    string = input().split()
    result = list()
    for char in string:
        if result and char in result[-1]:
            result[-1].append(char)
        else:
            result.append([char])
    print(result)


if __name__ == '__main__':
    main()
