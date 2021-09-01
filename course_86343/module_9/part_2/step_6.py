"""
Странное увлечение

Как известно, математики странные люди. Не составляет исключения и Тимур — автор данного курса.
Каждый день Тимур решает ровно две сложные математические задачи.
 Решая первую задачу, он записывает на первом листочке все числа, которые в ней встречаются.
 Далее он делает паузу и берется за вторую задачу.
 Затем записывает на втором листочке все числа, которые в ней встречаются.
 После этого он берет еще один листок и выписывает на него все совпадающие числа из первых двух листочков.
 Если такие числа есть, день удался, если общих чисел нет, Тимур считает день неудачным.

Напишите программу, которая находит общие числа двух листочков или сообщает, что день не удался 😏

Формат входных данных
На вход программе подаются две строки с числами: в первой строке числа с первого листочка, во второй со второго.

Формат выходных данных
Программа должна вывести числа, встретившиеся на обоих листках в отсортированном по убыванию порядке,
либо словосочетание BAD DAY, если таких чисел нет.
"""
import sys

DEBUG = False


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def main():
    set_1, set_2 = (set(map(int, input().split())) for _ in range(2))
    result = set_1 & set_2
    print(*sorted(result, reverse=True)) if result else print('BAD DAY')


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
