"""
Города

Тимур и Руслан играют в игру города. Они очень любят эту игру и знают много городов, особенно Тимур,
однако к концу игры ввиду своего возраста забывают, какие города уже называли.

Напишите программу, считывающую информацию об игре и сообщающую ребятам, что очередной город назван повторно.

Формат входных данных
На вход программе в первой строке подаётся натуральное число n – количество названных городов,
в последующих nn строках вводятся названные города и ещё одна строка с новым, только что названым городом.

Формат выходных данных
Программа должна вывести OK, если этот город ещё не вспоминали, и REPEAT, если город уже был назван.
"""
import sys

DEBUG = False


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def main():
    cities = [input() for _ in range(int(input()))]
    print('REPEAT' if input() in cities else 'OK')


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
