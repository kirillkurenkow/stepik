"""
Общие числа

На вход программе подаются две строки текста, содержащие числа.
Напишите программу, которая выводит все числа в порядке возрастания, которые есть как в первой строке, так и во второй.

Формат входных данных
На вход программе подаются две строки текста, содержащие числа, отделенные символом пробела.

Формат выходных данных
Программа должна вывести множество чисел, встречающихся в обеих строках.
"""
import sys

DEBUG = True


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def main():
    set_1 = set(map(int, input().split()))
    set_2 = set(map(int, input().split()))
    print(*sorted(set_1 & set_2))


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
