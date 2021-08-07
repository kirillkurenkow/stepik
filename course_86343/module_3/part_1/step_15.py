"""
Предикат делимости
Напишите функцию func(num1, num2), принимающую в качестве аргументов два натуральных числа num1 и num2
и возвращающую значение True если число num1 делится без остатка на число num2 и False в противном случае.

Результатом вывода программы должно быть "делится" (если функция func() вернула True) и
"не делится" (если функция func() вернула False).

Примечание. Следующий программный код:

print(func(10, 2))
print(func(5, 7))
print(func(15, 15))

должен выводить:

True
False
True

а вся программа должна выводить:

делится
не делится
делится
"""
DEBUG = True
if DEBUG:
    import sys

    sys.stdin = open('input.txt', encoding='utf-8')


def func(number_1: int, number_2: int) -> bool:
    return number_1 % number_2 == 0


def main():
    number_1, number_2 = [int(input()) for _ in range(2)]
    if func(number_1, number_2):
        print('делится')
    else:
        print('не делится')


if __name__ == '__main__':
    main()
