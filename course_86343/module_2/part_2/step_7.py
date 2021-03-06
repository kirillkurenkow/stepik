"""
Камень, ножницы, бумага
Тимур и Руслан пытаются разделить фронт работы по курсу "Python для профессионалов".
Для этого они решили сыграть в камень, ножницы и бумагу. Помогите ребятам бросить честный жребий и определить,
кто будет делать очередной модуль нового курса.

Формат входных данных
На вход программе подаются две строки текста, содержащие слова "камень", "ножницы" или "бумага".
На первой строке записан выбор Тимура, на второй – выбор Руслана.

Формат выходных данных
Программа должна вывести результат жеребьёвки, то есть кто победит Тимур, Руслан или они сыграют вничью.

Примечание. Правила игры стандартные: камень побеждает ножницы, но проигрывает бумаге, а ножницы побеждают бумагу.
"""
DEBUG = False
if DEBUG:
    import sys

    sys.stdin = open('input.txt')


def main():
    paper = 'бумага'
    scissors = 'ножницы'
    stone = 'камень'
    timur = 'Тимур'
    ruslan = 'Руслан'
    input_1, input_2 = input(), input()
    if input_1 == input_2:
        print('ничья')
    else:
        if input_1 == paper:
            if input_2 == stone:
                print(timur)
            else:
                print(ruslan)
        elif input_1 == stone:
            if input_2 == scissors:
                print(timur)
            else:
                print(ruslan)
        else:
            if input_2 == paper:
                print(timur)
            else:
                print(ruslan)


if __name__ == '__main__':
    main()
