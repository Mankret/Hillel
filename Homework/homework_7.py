# Дан словарь, создать новый словарь при помощи конструкции генератор словаря, поменяв местами ключ и значение.


some_dict = {1: 'Avalon', 2: 'Babylon', 3: 'Byzantium', 4: 'Empire'}
generation_dict = {v: k for k, v in some_dict.items()}

print(some_dict, generation_dict, sep='\n')


