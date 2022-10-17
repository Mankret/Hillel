# Дан словарь, создать новый словарь при помощи конструкции генератор словаря, поменяв местами ключ и значение.


some_dict = {'Avalon': 1, 'Babylon': 2, 'Byzantium': 3, 'Empire': 4}
generation_dict = {v: k for k, v in some_dict.items()}

print(some_dict, generation_dict, sep='\n')

