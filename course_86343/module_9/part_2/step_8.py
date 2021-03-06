"""
Онлайн-школа BEEGEEK 2

Каждый ученик, обучающийся в онлайн-школе BEEGEEK изучает либо математику, либо информатику, либо оба эти предмета.
У руководителя школы есть списки изучающих каждый предмет.

Напишите программу, позволяющую руководителю выяснить, сколько учеников изучает только математику.

Формат входных данных
На вход программе в первых двух строках подаются числа m и n – количества учеников,
изучающих математику и информатику соответственно.
Далее идут m строк — фамилии учеников, которые изучают математику и n строк с фамилиями учеников, изучающих информатику.

Формат выходных данных
Программа должна вывести количество учеников, которые изучают только математику.

Примечание. Гарантируется, что среди учеников школы BEEGEEK нет однофамильцев.
"""
import sys

DEBUG = False


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def main():
    m, n = int(input()), int(input())
    m_lines = {input() for _ in range(m)}
    n_lines = {input() for _ in range(n)}
    print(len(m_lines - n_lines))


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
