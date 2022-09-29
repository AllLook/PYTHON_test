x = float(input("Введите координату x:"))
y = float(input("Введите координату y:"))
if x != 0 and y !=0:
    if x > 0 and y > 0:
        print(1)
    elif x < 0 and y > 0:
        print(2)
    elif x < 0 and y < 0:
        print(3)
    elif x > 0 and y < 0:
        print(4)
else:
    print("Error") # на случай если будет введен 0 или 0.0