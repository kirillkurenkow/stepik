"""
Ходы ферзя

На шахматной доске 8 × 8 стоит ферзь. Отметьте положение ферзя на доске и все клетки, которые бьет ферзь.
Клетку, где стоит ферзь, отметьте буквой Q, клетки, которые бьет ферзь, отметьте символами *,
остальные клетки заполните точками.

Формат входных данных
На вход программе подаются координаты ферзя на шахматной доске в шахматной нотации (то есть в виде e4,
где сначала записывается номер столбца (буква от a до h, слева направо),
затем номер строки (цифра от 1 до 8, снизу вверх)).

Формат выходных данных
Программа должна вывести на экран изображение доски, разделяя элементы пробелами.
"""
import sys
from typing import List, Any

DEBUG = False
T_MATRIX = List[List[Any]]


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def print_matrix_with_spaces(matrix: T_MATRIX) -> None:
    [print(*row) for row in matrix]


def main():
    alphabet = 'abcdefgh'
    cords = input()
    cords = 8 - int(cords[1]), alphabet.find(cords[0])
    matrix = [['.' for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            # if i == 6 and j == 2:
            #     print()
            if (i == cords[0]) or (j == cords[1]) or (abs(cords[0] - i) == abs(cords[1] - j)):
                matrix[i][j] = '*'
    matrix[cords[0]][cords[1]] = 'Q'
    print_matrix_with_spaces(matrix)


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
