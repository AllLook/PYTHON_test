
import random
num = int(input("Введите размер строки:"))
st = str(input("Введите элемент строки:"))
my_list = []


def creation_list(num, st):
    for i in range(num):
        leters = random.sample(st, 3)
        my_list.append("".join(leters))  # чтобы небыло списка списков
    return " ".join(my_list)  # распоковка списка


def word_filter(my_list):
    result = []
    for i in range(len(my_list)):
        if st not in my_list[i]:
            # print(my_list[i])
            # добавление соответствующего условию элемента в список
            result.append(my_list[i])
    return " ".join(result)  # распоковка результата


print(creation_list(num, st))
print(word_filter(my_list))





