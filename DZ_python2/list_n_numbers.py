""" n = int(input("Введите кол-во чисел в списке:"))
sum = 0
my_list = []
for i in range(n):
    el = round((1 + 1/n)**n) #вот так все время одинаковые числа, но по условию такая формула
    my_list.append(el)
    sum += el
print(my_list)
print(sum) """


n = int(input("Введите кол-во чисел в списке:"))
sum = 0  # переменная для результата
my_list = []  # список
for i in range(1, n + 1):  # сдвиг диапазона чтобы не делить на 0 с ошибкой
    el = round((1 + 1/i)**i)  # текущий элемент
    my_list.append(el)  # добавление в список
    sum += el  # итог
print(my_list)
print(sum)
