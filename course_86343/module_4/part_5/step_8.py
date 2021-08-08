"""
Ходы коня

На шахматной доске 8 × 8 стоит конь. Напишите программу, которая отмечает положение коня на доске и все клетки,
которые бьет конь. Клетку, где стоит конь, отметьте английской буквой N, клетки, которые бьет конь,
отметьте символами *, остальные клетки заполните точками.

Формат входных данных
На вход программе подаются координаты коня на шахматной доске в шахматной нотации
(то есть в виде e4, где сначала записывается номер столбца (буква от a до h, слева направо),
затем номеру строки (цифра от 1 до 8, снизу вверх)).

Формат выходных данных
Программа должна вывести на экран изображение доски, разделяя элементы пробелами.
"""
import sys
import os

DEBUG = True
if DEBUG:
    input_filename = 'input.txt'
    if os.path.exists(input_filename):
        sys.stdin = open(input_filename, encoding='utf-8')


def main():
    matrix = [['.' for _ in range(8)] for _ in range(8)]
    knight = input()
    knight_cords = (8 - int(knight[1]), 'abcdefgh'.find(knight[0]))
    matrix[knight_cords[0]][knight_cords[1]] = 'N'
    for i in range(8):
        for j in range(8):
            if abs((knight_cords[1] - j) * (knight_cords[0] - i)) == 2:  # Формулу поиска взял из комментариев
                matrix[i][j] = '*'
    [print(*row) for row in matrix]


if __name__ == '__main__':
    main()
