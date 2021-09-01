"""
Все 10 цифр

На вход программе подаются две строки, состоящие из цифр.
Необходимо определить, верно ли, что в записи этих двух строк используются все десять цифр?

Формат входных данных
На вход подаются две строки, состоящие из цифр.

Формат выходных данных
Программа должна вывести YES, если в записи этих двух строк используются все десять цифр, и NO в противном случае.
"""
import sys

DEBUG = False


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def main():
    input_1, input_2 = input(), input()
    print('YES' if set(input_1 + input_2) == set(map(str, range(10))) else 'NO')


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
