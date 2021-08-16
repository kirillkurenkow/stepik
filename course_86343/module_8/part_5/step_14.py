"""
Встречалось ли число раньше?

На вход программе подается строка текста, содержащая числа.
Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности или NO,
если не встречалось.

Формат входных данных
На вход программе подается строка текста, содержащая числа, разделенные символом пробела.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Ведущие нули в числах должны игнорироваться.
"""
import sys

DEBUG = True


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def main():
    numbers = list(map(int, input().split()))
    result = set()
    for number in numbers:
        print('YES' if number in result else 'NO')
        result.add(number)


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
