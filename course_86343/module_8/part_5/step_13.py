"""
Количество слов в тексте
Напишите программу для определения общего количества различных слов в строке текста.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести одно число – общее количество различных слов в строке без учета регистра.

Примечание 1. Словом считается последовательность непробельных символов, идущих подряд,
слова разделены одним или большим числом пробелов.

Примечание 2. Знаками препинания .,;:-?! пренебрегаем.
"""
import sys

DEBUG = False


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def main():
    words = [x.strip('.,;:-?!') for x in input().lower().split()]
    if DEBUG:
        print(set(words))
    print(len(set(words)))


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
