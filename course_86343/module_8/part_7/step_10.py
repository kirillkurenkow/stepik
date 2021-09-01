"""
Урок информатики

Даны по 10-балльной шкале оценки по информатике трех учеников.
Напишите программу, которая выводит множество оценок, которые есть и у первого и второго учеников,
но которых нет у третьего ученика.

Формат входных данных
На вход программе подаются оценки трех учеников, разделенные символом пробела
(оценки каждого ученика на отдельной строке).

Формат выходных данных
Программа должна вывести множество оценок в порядке убывания на одной строке, разделенных пробелами,
в соответствии с условием задачи.

Примечание. Оценка ученика находится в диапазоне от 0 до 10 включительно.
"""
import sys

DEBUG = False


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def main():
    set_1, set_2, set_3 = (set(map(int, input().split())) for _ in range(3))
    print(*sorted((set_1 & set_2) - set_3, reverse=True))


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
