import math
numbers = float(input("Введите число:"))
numbers = int(round(numbers))
numbers = math.fabs(numbers)


def multipliers(numbers):
    mult = []
    m = 2
    while numbers > 1:
        if numbers % m == 0:
            mult.append(m)
            numbers //= m
        else:
            m += 1
    return mult


print(multipliers(numbers))
