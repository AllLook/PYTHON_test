from itertools import groupby, starmap
from os import path


def in_rle(text="text_words.txt", code_text="text_code_words.txt"):
    # если есть файл для раскодирования но нет уже раскодированного
    if path.exists(text) and not path.exists(code_text):
        with open(text) as my_f_1, \
                open(code_text, "a") as my_f_2:  # открытие файла и другого файла на дозапись
            for i in my_f_1:  # строки из файла
                # групперует из строки кол-во буквы формирует в список,разбирает опять в строку и записавает во второй файл
                my_f_2.write(
                    "".join([f"{len(list(v))}{ch}"for ch, v in groupby(i)]))
    else:
        print("error")  # если с файлами что то не так


def ex_rle(file_name):
    if path.exists(file_name):  # если файл сущест
        with open(file_name) as my_f:  # открытие
            n = ""  # переменная пустой строки
            for k in my_f:  # прогон по строкам
                my_list = []
                for i in k.strip():  # копия строки и ее разбор
                    if i.isdigit():  # является ли текущ элемент цифрой
                        n += i  # если цифра то увелич счетчик b сумм значение
                    else:
                        # если цифр в строке нет то n будет false(0) для текущ элемента
                        my_list.append([int(n), i])
                        n = ""  # обнуляется n
                # умножаем букву на цифру и разбираем в строку
                print("".join(starmap(lambda x, y: x * y, my_list)))

    else:
        print("error")
