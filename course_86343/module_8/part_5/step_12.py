"""
Уникальные символы 2

Напишите программу для вывода общего количества уникальных символов во всех считанных словах без учета регистра.

Формат входных данных
На вход программе в первой строке подается число n – общее количество слов. Далее идут n строк с словами.

Формат выходных данных
Программа должна вывести одно число – общее количество уникальных символов во всех словах без учета регистра.
"""
import sys

DEBUG = False


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def main():
    print(len(set(''.join((input().lower() for _ in range(int(input())))))))


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
