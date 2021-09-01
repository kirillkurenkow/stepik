"""
Три слова

На вход программе подается строка, состоящая из трех слов.
Верно ли, что для записи всех трех слов был использован один и тот же набор букв?

Формат входных данных
На вход программе подается строка, состоящая из трех слов.

Формат выходных данных
Программа должна вывести YES, если для записи всех трех слов был использован один и тот же набор букв и NO
в противном случае.
"""
import sys

DEBUG = False


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def main():
    inputs = input().split()
    print('YES' if set(inputs[0]) == set(inputs[1]) == set(inputs[2]) else 'NO')


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
