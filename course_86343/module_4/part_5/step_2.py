"""
Максимум в таблице

На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрице,
затем n строк по m целых чисел в каждой, отделенных символом пробела.

Напишите программу, которая находит индексы (строку и столбец) первого вхождения максимального элемента.

Формат входных данных
На вход программе на разных строках подаются два числа n и m — количество строк и столбцов в матрице, з
атем сами элементы матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести два числа: номер строки и номер столбца, в которых стоит наибольший элемент таблицы.
Если таких элементов несколько, то выводится тот, у которого меньше номер строки, а если номера строк равны то тот,
у которого меньше номер столбца.

Примечание. Считайте, что нумерация строк и столбцов начинается с нуля.
"""
import sys
import os

DEBUG = False
if DEBUG:
    input_filename = 'input.txt'
    if os.path.exists(input_filename):
        sys.stdin = open(input_filename, encoding='utf-8')


def main():
    n, m = map(int, (input() for _ in range(2)))
    matrix = [list(map(int, input().split())) for _ in range(n)]
    max_element = max((max(row) for row in matrix))
    if DEBUG:
        print(max_element)
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if element == max_element:
                print(i, j)
                return


if __name__ == '__main__':
    main()
