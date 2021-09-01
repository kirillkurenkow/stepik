"""

"""
import sys
import os

DEBUG = False
if DEBUG:
    input_filename = 'input.txt'
    if os.path.exists(input_filename):
        sys.stdin = open(input_filename, encoding='utf-8')


def main():
    number = int(input())
    matrix = [list(map(int, input().split())) for _ in range(number)]
    upper, lower, left, right = list(), list(), list(), list()
    for i in range(number):
        for j in range(number):
            element = matrix[i][j]
            if j > i < number - 1 - j:
                upper.append(element)
            elif j < i > number - 1 - j:
                lower.append(element)
            elif j < i < number - 1 - j:
                left.append(element)
            elif j > i > number - 1 - j:
                right.append(element)
    print(f'Верхняя четверть: {sum(upper)}')
    print(f'Правая четверть: {sum(right)}')
    print(f'Нижняя четверть: {sum(lower)}')
    print(f'Левая четверть: {sum(left)}')


if __name__ == '__main__':
    main()
