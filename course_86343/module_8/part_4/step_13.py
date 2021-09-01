"""
Неповторимые цифры

На вход программе подается строка, состоящая из цифр.
Необходимо определить, верно ли, что в ее записи ни одна из цифр не повторяется?

Формат входных данных
На вход программе подается строка, состоящая из цифр

Формат выходных данных
Программа должна вывести YES, если ни одна из цифр в строке не повторяется и NO в противном случае.
"""
import sys

DEBUG = False


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def main():
    input_ = input()
    print('YES' if len(set(input_)) == len(input_) else 'NO')


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
