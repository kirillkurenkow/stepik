"""
Домашнее задание

Учитель проверяет домашнее задание в классе и получил следующие ответы: из n школьников у m домашнее задание
съела собака, у k отключили свет, а p учеников постигли оба несчастья.
Напишите программу, которая определяет сколько человек выполнило домашнее задание.

Формат входных данных
На вход программе подаются числа n, m, k, p, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести количество учеников, сделавших домашнее задание.
"""
import sys

DEBUG = True


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def main():
    n, m, k, p = (int(input()) for _ in range(4))
    print(n - m - k + p)


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
