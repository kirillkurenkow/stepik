"""
Телефонная книга

Тимур записал телефоны всех своих друзей, чтобы автоматизировать поиск нужного номера.

У каждого из друзей Тимура может быть один или более телефонных номеров.
Напишите программу, которая поможет Тимуру находить все номера определённого друга.

Формат входных данных
В первой строке задано одно целое число nn — количество номеров телефонов,
информацию о которых Тимур сохранил в телефонной книге.
В следующих nn строках заданы телефоны и имена их владельцев через пробел.
В следующей строке записано целое число mm — количество поисковых запросов от Тимура.
В следующих mm строках записаны сами запросы, по одному на строке. Каждый запрос — это имя друга,
чьи телефоны Тимур хочет найти.

Формат выходных данных
Для каждого запроса от Тимура выведите в отдельной строке все телефоны,
принадлежащие человеку с этим именем (независимо от регистра имени).
Если в телефонной книге нет телефонов человека с таким именем,
выведите в соответствующей строке «абонент не найден» (без кавычек).

Примечание 1.
Телефоны одного человека выводите в одну строку через пробел в том порядке, в каком они были заданы во входных данных.

Примечание 2.
Количество строк в ответе должно быть равно числу mm.

Примечание 3.
Телефон — это несколько цифр, записанных подряд, а имя может состоять из букв русского или английского алфавита.
Записи не повторяются.
"""
import sys

DEBUG = False


def set_debug_input():
    input_filename = 'input.txt'
    sys.stdin = open(input_filename, encoding='utf-8')


def main():
    phones = {}
    for _ in range(int(input())):
        phone, name = input().lower().split()
        if name in phones:
            phones[name].append(phone)
        else:
            phones[name] = [phone]
    [print(' '.join(phones.get(input().lower(), ['абонент не найден']))) for _ in range(int(input()))]


if __name__ == '__main__':
    if DEBUG:
        set_debug_input()
    main()
