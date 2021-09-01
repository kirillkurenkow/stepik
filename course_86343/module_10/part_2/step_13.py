"""
Строковое представление

Напишите программу, которая будет превращать натуральное число в строку, заменяя все цифры в числе на слова:
    * 0 на zero;
    * 1 на one;
    * 2 на two;
    * 3 на three;
    * 4 на four;
    * 5 на five;
    * 6 на six;
    * 7 на seven;
    * 8 на eight;
    * 9 на nine.

Формат входных данных
На вход программе подается натуральное число.

Формат выходных данных
Программа должна вывести строковое представление числа.

Примечание. Используйте словарь вместо условного оператора.
"""
import sys

DEBUG = False


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def main():
    numbers = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
    }
    print(*(numbers[int(number)] for number in input()))


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
