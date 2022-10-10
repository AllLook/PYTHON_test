""" number = float(input("Введите число реальное:"))
accuracy = input("Введите требуемую точность '0.0001':").split(".")
acc = accuracy[1]
print(acc)
print(f"{number:.{len(acc)}f}") """


from decimal import Decimal
number = float(input("Введите число реальное:"))
accuracy = input("Введите требуемую точность '0.0001':")


def acc(number, accuracy):
    number = Decimal(f"{number}")  # создание строкового обьекта Docimal
    # округление с заданным кол вом знаков из number
    return number.quantize(Decimal(f"{accuracy}"))


print(acc(number, accuracy))
