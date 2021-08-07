"""
Задача Иосифа Флавия
nn человек, пронумерованных числами от 11 до n, стоят в кругу. Они начинают считаться,
каждый k-й по счету человек выбывает из круга, после чего счет продолжается со следующего за ним человека.
Напишите программу, определяющую номер человека, который останется в кругу последним.

Формат входных данных
На вход программе подаются два числа n и k, записанные на отдельных строках.

Формат выходных данных
Программа должна вывести одно число – номер человека, который останется в кругу последним.
"""


def main():
    n, k = (int(input()) for _ in range(2))
    items_list = list(range(1, n + 1))
    index_to_remove = (k - 1) % len(items_list)
    while len(items_list) > 1:
        for index, item in enumerate(items_list):
            if index == index_to_remove:
                items_list.pop(index)
                index_to_remove = (index_to_remove + k - 1) % len(items_list)
                break
    print(items_list[0])


if __name__ == '__main__':
    main()
