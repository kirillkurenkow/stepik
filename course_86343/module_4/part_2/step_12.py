"""
Дополните приведенный код, используя списочный метод append(), чтобы список list1 имел вид:

list1 = [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
"""
DEBUG = True
if DEBUG:
    import sys

    sys.stdin = open('input.txt', encoding='utf-8')


def main():
    list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
    list1[2][2].append(7000)
    print(list1)


if __name__ == '__main__':
    main()
