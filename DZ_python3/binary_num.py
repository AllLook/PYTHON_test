num = int(input("Введите десятичное число:"))


def BinaryNum(num):
    my_list = []
    while num > 0:  # пока число не кончится
        # остаток от деления добавляем в список после 0
        my_list.insert(0, num % 2)
        num //= 2  # num становится равен частному
    print(*my_list, sep="")


print(BinaryNum(num))
