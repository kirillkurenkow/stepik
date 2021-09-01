"""
Каждый n-ый элемент

На вход программе подается строка текста, содержащая символы и число n. Из данной строки формируется список.
Напишите программу, которая разделяет список на вложенные подсписки так,
что n последовательных элементов принадлежат разным подспискам.

Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела и число n на отдельной строке.

Формат выходных данных
Программа должна вывести указанный вложенный список.
"""
import sys

DEBUG = False


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def main():
    input_list = input().split()
    number = int(input())
    result = list()
    for i in range(number):
        row = [input_list[j] for j in range(i, len(input_list), number)]
        result.append(row)
    print(result)


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
