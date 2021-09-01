"""
Книги на прочтение

Руслан получил в конце учебного года список литературы на лето.
Теперь ему надо выяснить, какие книги из этого списка у него есть.
У Руслана на компьютере в текстовом файле записаны все книги из его домашней библиотеки в случайном порядке.

Напишите программу, определяющую для каждой книги из списка на прочтение, есть она у Руслана или нет.

Формат входных данных
На вход программе в первой строке подается натуральное число mm — количество книг в домашней библиотеке Руслана.
Во второй строке записано натуральное число n —  количество книг в списке на лето.
Далее идут m строк с названиями книг из домашней библиотеки и n строк названий из списка на лето.

Формат выходных данных
Программа должна вывести n строк, в каждой из которых написано слово YES, если книга найдена в библиотеке,
и NO, если нет.
"""
import sys

DEBUG = False


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def main():
    books_library_count = int(input())
    books_for_summer_count = int(input())
    books_library = [input() for _ in range(books_library_count)]
    books_for_summer = [input() for _ in range(books_for_summer_count)]
    [print(('NO', 'YES')[book in books_library]) for book in books_for_summer]


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
