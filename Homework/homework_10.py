# Дан список состоящий из данных разного типа.
# Вернуть новый список, где при помощи функции map() каждый элемент типа int первоначального списка приведён к типу str,
# элементы всех остальных типов передаются в новый список без изменения их типа.
# В качестве входной функции в map() использовать lambda-функцию.
# values = [1, 2, '3', 'forth', 'end', 99, True, None]

values = [1, 2, '3', 'forth', 'end', 99, True, None]

new_list = (list(map(lambda x: str(x), (values[0], values[1], values[5]))))
values[0] = new_list[0]
values[1] = new_list[1]
values[5] = new_list[2]
new_list = values


print(new_list)

