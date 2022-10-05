num = int(input("Введите размер списка:"))
my_list = []
for i in range(num):
    i = int(input("Введите число списка:"))
    my_list.append(i)
print(my_list)


def odd(my_list):
    sum = my_list[0]

    for k in range(1, num):
        if k % 2 == 0:
            sum += my_list[k]

    return sum


print(odd(my_list))

""" from random import sample  # метод sample из random
def list_rand_nums(count: int):  # определение типа
    if count < 0:
        print("Error numbers")  # если отрицательное число для длинны
        return []  # возвращаем пустой список
    # из последовательности кол-во случайных элементов
    list_nums = sample(range(1, count * 2), count)
    return list_nums


def sum_odd_pos(list_nums: list):  # передаем список
    sum_nums = 0  # переменная для результата
    # цикл прохождения по элементам списка с шагом 2(т.е через 1)
    for k in range(0, len(list_nums), 2):
        sum_nums += list_nums[k]  # прибавляем текущий элемент из списка
    return sum_nums


# вводим переменную для сохранения в ней списка
all_list = list_rand_nums(int(input("Numbers:")))
print(all_list)  # печать списка
print(sum_odd_pos(all_list))  # результат """
