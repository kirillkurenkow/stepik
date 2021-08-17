"""
Онлайн-школа BEEGEEK 6 🌶️

Руководителю онлайн-школы BEEGEEK захотелось узнать,
кто из его учеников присутствовал на всех уроках с начала учебного года.
Для каждого урока есть листок со списком присутствовавших учеников.

Напишите программу, определяющую фамилии учеников, которые присутствовали на всех уроках.

Формат входных данных
На вход программе в первой строке дается число m – количество уроков, проведенных с начала учебного года.
Далее идёт m блоков строк, описывающих листки с фамилиями.
На первой строке каждого блока указано количество фамилий n_i, затем идёт n_i строчек с фамилиями тех,
кто был на уроке i-ом уроке.

Формат выходных данных
Программа должна вывести фамилии учеников, которые были на всех уроках, отсортированных в лексикографическом порядке.
Каждая фамилия должна быть записана на отдельной строке.

Примечание 1. Гарантируется, что среди учеников школы BEEGEEK нет однофамильцев.

Примечание 2. Гарантируется, что хотя бы один ученик был на всех уроках.
"""
import sys

DEBUG = True


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def main():
    lessons_count = int(input())
    names = [{input() for _ in range(int(input()))} for _ in range(lessons_count)]
    print(*sorted(names[0].intersection(*names[1:])), sep='\n')


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
