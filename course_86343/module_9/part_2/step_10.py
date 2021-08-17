"""
Онлайн-школа BEEGEEK 4

Руководитель онлайн-школы BEEGEEK и его помощник составили списки учеников их школы.

Напишите программу, которая выведет все фамилии учеников, которые вспомнили руководитель и его помощник.

Формат входных данных
На вход программе в первой строке подаются фамилии, записанные руководителем школы,
а на второй строке - помощником руководителя. Фамилии указываются через пробел.

Формат выходных данных
Программа должна вывести все фамилии учеников, отсортированных в лексикографическом порядке,
записанные руководителем и его помощником.

Примечание. Гарантируется, что среди учеников школы BEEGEEK нет однофамильцев.
"""
import sys

DEBUG = True


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def main():
    set_1 = set(input().split())
    set_2 = set(input().split())
    print(*sorted(set_1 | set_2))


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()