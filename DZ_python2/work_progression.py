num = int(input("Введите целое число:"))
sum = 1
i = 0
while i < num:
    sum *= i + 1
    print(sum)
    i += 1
""" for i in range(num)#range до num потому что нужно до числа, само число умножать не надо
    sum *= i + 1 #range начинается с 0 поэтому первый вывод 1
    print(sum)  """
