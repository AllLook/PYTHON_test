from random import sample,choice

num1 = int(input("Введите длинну списка:"))
#my_list1 = sample(range(1, num1*2), num1)
for i in range(num1):
    my_list1 = []
    i = choice(range(num1*2))
    my_list1.append(i)
print(my_list1)


""" def WorkCouples(my_list1):

    my_list2 = []
    for k in range(len(my_list1)//2):  # или num1 // 2
        k = my_list1[k] * my_list1[-1-k]
        my_list2.append(k)

    if len(my_list1) % 2 != 0:

        # my_list2.append(my_list1[len(my_list1//2)])
        my_list2.append(my_list1[num1//2])

    return my_list2


print(WorkCouples(my_list1)) """
