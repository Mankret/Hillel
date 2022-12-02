# Основной файл!#детальная запись данных ввода( имя, фамилия, дата рождения, дата смерти, пол

from Implementation import Main
from persontest import Person


person = Person()
data = Main()
while True:

    start = input("""  
    * Чтение данные (load, l, чтение, ч):                       
    * Записать данные (record, r, записать, з):                  
    * Произвести поиск по существующим данным (search,s, поиск, п):                 
    * Выход: (выход, exit, quit, e, q) : 
    * Сохранить данные в csv файл (save, сохранить, с): """)

    if start.lower() in ('load', 'l', 'чтение', 'ч'):

        person.load()
        continue
    elif start.lower() in ('record', 'r', 'записать', 'з'):
        person.recording()
    elif start.lower() in ('search', 's', 'поиск', 'п'):
        person.search()

    elif start.lower() in ('save', 'сохранить', 'с'):
        person.save_to_file()
    elif start.lower() in ('выход', 'exit', 'quit', 'e', 'q'):
        person.save_to_file()
        break


