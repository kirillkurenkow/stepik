"""
Набор сообщений

На мобильных кнопочных телефонах текстовые сообщения можно отправлять с помощью цифровой клавиатуры.
Поскольку с каждой клавишей связано несколько букв, для большинства букв требуется несколько нажатий клавиш.
При однократном нажатии цифры генерируется первый символ, указанный для этой клавиши.
Нажатие цифры 2, 3, 4 или 5 раз генерирует второй, третий, четвертый или пятый символ клавиши.

                1	.,?!:
                2	ABC
                3	DEF
                4	GHI
                5	JKL
                6	MNO
                7	PQRS
                8	TUV
                9	WXYZ
                0	space (пробел)

Напишите программу, которая отображает нажатия клавиш, необходимые для введенного сообщения.
"""
import sys

DEBUG = False


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def main():
    string = input().upper()
    keys_mapping = {
        '.,?!:': '1',
        'ABC': '2',
        'DEF': '3',
        'GHI': '4',
        'JKL': '5',
        'MNO': '6',
        'PQRS': '7',
        'TUV': '8',
        'WXYZ': '9',
        ' ': '0',
    }
    for element in string:
        for key in keys_mapping:
            if element in key:
                print(keys_mapping[key] * (key.find(element) + 1), end='')
    print()


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
