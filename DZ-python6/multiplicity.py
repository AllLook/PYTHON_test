num = int(input("Введите число порога:"))


def multiplicity(num):

    my_list = []
    mul1 = 20
    my_list.append(mul1)
    mul2 = 21
    my_list.append(mul2)
    [my_list.append(i) for i in range(22, num + 1) if i % mul1 == 0 or i % mul2 == 0]
    return my_list

    # print(my_list)
print(multiplicity(num))


""" num = int(input("Введите число порога:"))
def multiplicity(num):
    return[i for i in range(20,num + 1) if i % 20 == 0 or i % 21 == 0] 
print(multiplicity(num)) """
