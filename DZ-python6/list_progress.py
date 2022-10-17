import numbers
from random import sample
numbers = int(input("Введите длинну списка:"))


def progress(numbers):
    in_list = sample(range(numbers*3), numbers)
    print(in_list)
    return [in_list[i] for i in range(1, len(in_list)) if in_list[i] > in_list[i - 1]]


print(progress(numbers))
