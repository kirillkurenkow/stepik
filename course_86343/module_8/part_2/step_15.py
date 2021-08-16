"""
Книги на прочтение 🌶️
Ученики 1010 класса онлайн-школы BEEGEEK получили задание прочесть на летних каникулах три книги:
    * "Что такое математика?";
    * "Математическая составляющая";
    * "100 гениальных идей по математике".

Оказалось, что n учеников прочитали первую книгу, m учеников — вторую, k учеников — третью.
Также известно, что x учеников прочли первую или вторую, или обе эти книги, y учеников — вторую или третью, или обе,
z учеников — первую и третью, или хотя бы одну из этих двух книг. Полностью выполнили задание только t учеников.
Всего в 10 классе учится a учеников.

Напишите программу, которая выводит сколько учеников:
    * прочитали только одну книгу;
    * прочитали две книги;
    * не прочитали ни одной из рекомендованных книг.

Формат входных данных
На вход программе подаются числа n, m, k, x, y, z, t, a, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести три числа в соответствии с условием задачи, каждое на отдельной строке.
"""
import sys

DEBUG = True


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def main():
    n, m, k, x, y, z, t, a = map(int, (input() for _ in range(8)))
    nm = n + m - x
    mk = m + k - y
    kn = k + n - z
    one_book = (n - nm - kn + t) + (k - kn - mk + t) + (m - mk - nm + t)
    two_books = nm + mk + kn - t * 3
    print(one_book)
    print(two_books)
    print(a - t - one_book - two_books)


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()