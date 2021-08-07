"""
Назад, вперёд и наоборот
На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел.
Напишите программу, которая меняет местами соседние элементы списка (a[0] c a[1], a[2] c a[3] и т.д.).
Если в списке нечетное количество элементов, то последний остается на своем месте.

Формат входных данных
На вход программе подается строка текста, содержащая натуральные числа, разделенные пробелами.

Формат выходных данных
Программа должна вывести измененный список, разделяя его элементы одним пробелом.
"""
DEBUG = True
if DEBUG:
    import sys

    sys.stdin = open('input.txt')


def main():
    numbers = [int(x) for x in input().split()]
    numbers = [numbers[i:i + 2] for i in range(0, len(numbers), 2)]
    new_numbers = list()
    for section in numbers:
        new_numbers.extend(reversed(section))
    print(*new_numbers)


if __name__ == '__main__':
    main()
