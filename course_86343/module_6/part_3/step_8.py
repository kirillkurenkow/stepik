"""
Вершина параболы
Уравнение параболы имеет вид y = ax^2 + bx + c, где a!=0.
Напишите программу, которая по введенным значениям a, b, c определяет и выводит вершину параболы.

Формат входных данных
На вход программе подаются три целых числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести координаты вершины параболы.
"""
import sys

DEBUG = True


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def main():
    a, b, c = map(int, (input() for _ in range(3)))
    cords = -(b / (2 * a)), (4 * a * c - b ** 2) / (4 * a)
    print(cords)


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
