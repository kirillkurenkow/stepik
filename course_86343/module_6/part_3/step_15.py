"""
Последовательность Трибоначчи

Напишите программу, которая считывает натуральное число nn и выводит первые nn чисел последовательности Трибоначчи.

Формат входных данных
На вход программе подается одно число n, n ≤ 100 – количество членов последовательности.

Формат выходных данных
Программа должна вывести члены последовательности Трибоначчи, отделенные символом пробела.

Примечание. Последовательность Трибоначчи – последовательность натуральных чисел,
где каждое последующее число является суммой трех предыдущих.
"""
import sys

DEBUG = True


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def tribonacci():
    numbers = [1, 1, 1]
    while True:
        numbers.append(sum(numbers[-3:]))
        yield numbers


def main():
    number = int(input())
    if number < 4:
        print(*(1, 1, 1)[:number])
    else:
        numbers = tribonacci()
        for _ in range(number - 4):
            next(numbers)
        print(*next(numbers))


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
