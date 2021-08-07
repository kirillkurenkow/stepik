"""
Роскомнадзор запретил букву а
Необходимо написать программу, реализующую алгоритм написания этой песни.
Алгоритм выводит в конце предложения следующую в алфавитном порядке букву, если она встречается в строке текста,
а очередную строку отображает уже без этой буквы.

Формат входных данных
На вход программе подается одно слово, записанное строчными русскими буквами без буквы "ё".

Формат выходных данных
Программа должна вывести в соответствии с указанным алгоритмом строки,
количество которых равно количеству разных букв в строке,
которая получается путем конкатенации введенного слова и строки "запретил букву".

Примечание 1. Текст исходной песни в первом тесте.

Примечание 2. Поем и решаем, друзья, поем и решаем.
"""
DEBUG = True
if DEBUG:
    import sys

    sys.stdin = open('input.txt', encoding='utf-8')


def main():
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    string = input() + ' запретил букву'
    for letter in alphabet:
        if letter in string:
            print(f'{string} {letter}')
            string = string.replace(letter, '').strip().replace('  ', ' ')


if __name__ == '__main__':
    main()
