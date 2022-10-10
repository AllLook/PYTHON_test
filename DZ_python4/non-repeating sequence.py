from random import sample
from random import randrange
count = int(input("Введите размер последовательности:"))
my_list = []
for i in range(count):
    my_list.append(randrange(count))
#my_list = sample(range(100), 10)
print(my_list)


def Sequence(my_list):
    result = []
    dict = {}
    for i in my_list:
        dict[i] = None
    for k in dict:
        result.append(k)
    return result


print(Sequence(my_list))
