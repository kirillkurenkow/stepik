"""
Разбиение на чанки
На вход программе подаются две строки, на одной символы, на другой число n. Из первой строки формируется список.

Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска),
а возвращает список из чанков указанной длины.

Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела и число n на отдельной строке.

Формат выходных данных
Программа должна вывести указанный вложенный список.

Примечание. Не забудьте вызвать функцию chunked(), чтобы вывести результат.
"""
import sys
import os

DEBUG = False
if DEBUG:
    input_filename = 'input.txt'
    if os.path.exists(input_filename):
        sys.stdin = open(input_filename, encoding='utf-8')


def chunked(items: list, chunk_size: int) -> list:
    result = [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]
    return result


def main():
    items = input().split()
    chunk_size = int(input())
    print(chunked(items, chunk_size))


if __name__ == '__main__':
    main()
