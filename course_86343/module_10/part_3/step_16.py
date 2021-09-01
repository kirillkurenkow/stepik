"""
Исправление дубликатов 🌶️

На вход программе подается строка, содержащая строки-идентификаторы.
Напишите программу, которая исправляет их так, чтобы в результирующей строке не было дубликатов.
Для этого необходимо прибавлять к повторяющимся идентификаторам постфикс _n, где n – количество раз,
сколько такой идентификатор уже встречался.

Формат входных данных
На вход программе подается строка текста, содержащая строки-идентификаторы, разделенные символом пробела.

Формат выходных данных
Программа должна вывести исправленную строку, не содержащую дубликатов сохранив при этом исходный порядок.
"""
import sys

DEBUG = False


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def main():
    string = input().split()
    printed = []
    for element in string:
        count_ = printed.count(element)
        print(element if not count_ else f'{element}_{count_}', end=' ')
        printed.append(element)


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
