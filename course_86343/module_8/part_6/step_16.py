"""
Общие цифры

На вход программе подается натуральное число n, а затем n различных натуральных чисел, каждое на отдельной строке.
Напишите программу, которая выводит все общие цифры в порядке возрастания у всех введенных чисел.

Формат входных данных
На вход программе подаются натуральное число n ≥ 1, а затем n различных натуральных чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести цифры в соответствии с условием задачи. Если общих цифр нет, то ничего выводить не нужно.
"""
import sys

DEBUG = False


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def main():
    set_list = [set(map(int, input())) for _ in range(int(input()))]
    result = set_list[0].intersection(*set_list[1:])
    if result:
        print(*sorted(result))


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
