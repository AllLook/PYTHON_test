name = str(input("Введите список имён:"))
def name_list(*name):  # создаем кортеж
    dict_name = {}
    for i in sorted(name):  # сортируем и прогоняем через цикл по очереди
        let = i[0]  # первая буква текущего имени
        if let in dict_name:  # если ключ(буква) есть в словаре
            dict_name[let] += [i]  # прибовляем текущие имя к значению
        else:
            dict_name[let] = [i]  # если нет то создаем ключ и значение к нему
    return dict_name

print(name_list(name))
