# Созадать словарь в качестве ключа которого будет 6-ти значное число, а в качестве значений кортеж состоящий из 2-х
# элементов – имя(str), возраст(int). Сделать около 5-6 элементов словаря. Записать данный словарь на диск в json-файл
import json

new_dict = {
    2312345: ('Joghn', 23),
    564765: ('Mike', 65),
    897654: ('Sandra', 32),
    445321: ('Lisbeth', 21),
    112233: ('Mikasa', 19),
}


with open('jsontest.json', 'w') as f:
    json.dump(new_dict, f)
