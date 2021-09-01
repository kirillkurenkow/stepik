"""
Одинаковые цифры

На вход программе подаются два числа. Напишите программу, определяющую, есть ли в данных числах одинаковые цифры.

Формат входных данных
На вход программе подаются два натуральных числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести YES, если в записи данных чисел есть одинаковые цифры и NO если нет.
"""
import sys

DEBUG = False


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def main():
    set_1, set_2 = set(input()), set(input())
    print('NO' if set_1.isdisjoint(set_2) else 'YES')


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
