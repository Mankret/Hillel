# Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные (4 функции input()).
# Создать файл и записать в него первые 2 строки и закрыть файл.
# Затем открыть файл на редактирование и дозаписать оставшиеся 2 строки.
# В итогом файле должны быть 4 строки, каждая из которых должна начинаться с новой строки.


first = input("First sentence: ")

second = input("Second sentence: ")

third = input("Third sentence: ")

fourth = input("Fourth sentence: ")


with open('new_file.txt', 'w') as new_f:
    new_f.write('%s\n' % first)
    new_f.write('%s\n' % second)

with open('new_file.txt', 'a') as new_f:
    new_f.write('%s\n' % third)
    new_f.write('%s\n' % fourth)

