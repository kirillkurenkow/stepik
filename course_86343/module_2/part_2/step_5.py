"""
Различные элементы
На вход программе подается строка текста, содержащая натуральные числа, расположенные по неубыванию.
Из строки формируется список чисел. Напишите программу для подсчета количества разных элементов в списке.

Формат входных данных
На вход программе подается строка текста, содержащая натуральные числа, разделенные символом пробела,
расположенные по неубыванию.

Формат выходных данных
Программа должна вывести одно число – количество различных элементов списка.

Примечание. Задачу можно решить без множеств.
"""
DEBUG = False
if DEBUG:
    import sys

    sys.stdin = open('input.txt')


def main():
    print(len(set(input().split())))


if __name__ == '__main__':
    main()
