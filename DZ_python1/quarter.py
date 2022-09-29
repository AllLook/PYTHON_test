quar = float(input("Введите номер четверти:"))
if quar > 0 and quar != 0 and quar < 5:
    if quar == 1:
        print("x > 0 , y > 0")
    elif quar == 2:
        print("x < 0 , y > 0")
    elif quar == 3:
        print("x < 0 , y < 0")
    elif quar == 4:
        print("x > 0 , y < 0")
else:
    print("error")
