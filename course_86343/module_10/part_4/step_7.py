"""
Секретное слово

Напишите программу для расшифровки секретного слова методом частотного анализа.

Формат входных данных
В первой строке задано зашифрованное слово. Во второй строке задано одно целое число nn – количество букв в словаре.
В следующих nn строках записано, сколько раз конкретная буква алфавита встречается в этом слове – <буква>: <частота>.

Формат выходных данных
Программа должна вывести дешифрованное слово.

Примечание. Гарантируется, что частоты букв не повторяются.
"""
import sys

DEBUG = False


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def main():
    encoded_string = input()
    encoded = {encoded_string.count(x): x for x in set(encoded_string)}
    chars = {int(y): x for _ in range(int(input())) for x, y in [input().split(': ')]}
    decode_table = {encoded[x]: y for x, y in chars.items()}
    print(*(decode_table[x] for x in encoded_string), sep='')


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
