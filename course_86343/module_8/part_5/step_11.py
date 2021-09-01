"""
Уникальные символы 1

Напишите программу для вывода количества уникальных символов каждого считанного слова без учета регистра.

Формат входных данных
На вход программе в первой строке подается число n – общее количество слов. Далее идут n строк с словами.

Формат выходных данных
Программа должна вывести на отдельной строке количество уникальных символов для каждого слова.
"""
import sys

DEBUG = False


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def main():
    [print(len(set(input().lower()))) for _ in range(int(input()))]


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
