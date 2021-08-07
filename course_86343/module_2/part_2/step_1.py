"""
Дан набор точек на координатной плоскости. Необходимо подсчитать и вывести количество точек,
лежащих в каждой координатной четверти.

Формат входных данных
В первой строке записано количество точек.
Каждая следующая строка состоит из двух целых чисел — координат точки (сначала абсцисса – x, затем ордината – y),
разделенных символом пробела.

Формат выходных данных
Программа должна вывести количество точек, лежащих в каждой координатной четверти, как в примерах.

Примечание. Учтите, что точки, лежащие на осях координат, не принято относить к какой либо координатной четверти.
"""
DEBUG = True
if DEBUG:
    import sys
    sys.stdin = open('input.txt')


def main():
    dots_count = int(input())
    dots = [[int(x) for x in input().split()] for _ in range(dots_count)]
    dots = [dot for dot in dots if 0 not in dot]
    first_quarter, second_quarter, third_quarter, forth_quarter = (list() for _ in range(4))
    for dot in dots:
        if dot[0] < 0:
            third_quarter.append(dot) if dot[1] < 0 else second_quarter.append(dot)
        else:
            forth_quarter.append(dot) if dot[1] < 0 else first_quarter.append(dot)
    print(f'Первая четверть: {len(first_quarter)}')
    print(f'Вторая четверть: {len(second_quarter)}')
    print(f'Третья четверть: {len(third_quarter)}')
    print(f'Четвертая четверть: {len(forth_quarter)}')


if __name__ == '__main__':
    main()
