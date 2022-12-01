# Хранение данных о человеке, проверка данных и возврат объекта с данными
# хранить данные в списке, в которое хранится словарь с информацией о человеке
# дабвление в список можно сделать через append()
# Убрать сохранение в файл
# добавить метод сохранения по запросу
#
#
#

#
import datetime
import json

from Implementation import Main
from datetime import date


data = Main()






class Person:

    @staticmethod
    def recording():

        while True:
            today = datetime.datetime.now()
            data_person = []
            message = 'Вы ввели не корректные данные'
            data_dict = {}
            data_list = []
            print("ВАЖНО!Вводите корректные данные, иначе придется повторять процедуру ввода заново!")

            name = input('Введите имя: ').title()
            if not name.isalpha():
                print(message)
                continue
            data_dict['name'] = name

            surname = input('Введите фамилию: ').title()
            if not surname.isalpha():
                print(message)
                continue
            data_dict['surname'] = surname

            second_name = input('Введите отчество: ').title()
            if not second_name.isalpha():
                print(message)
                continue
            data_dict['second name'] = second_name

            date_of_born = input('Введите дату рождения: ').replace('-', '.').replace('/', '.')
            if not date_of_born[0:].isdigit() and not date_of_born[-1:].isdigit():
                print(message)
                continue
            # date_born = datetime.datetime.strptime(date_of_born, '%d.%m.%Y')
            data_dict['date of born'] = date_of_born

            sex = input('Введите пол: ').title()
            if not sex.isalpha():
                print(message)
                continue
            data_dict['sex'] = sex

            date_of_death = input('Введите дату смерти, либо (н, n): ').replace('-', '.').replace('/', '.')
            if date_of_death.lower() in ('n', 'н'):
                # data_list.append(data_dict)
                data.save_to_list(data_dict)
                # data.save_file(data_dict)
                end = input('Данны сохранены, нажмите Enter для продолжения: ')
                offer = input('Введите (выход, exit, quit, e, q) для выхода: ')
                if offer.lower() in ('выход', 'exit', 'quit', 'e', 'q'):
                    break
            if not date_of_death[0:].isdigit() and not date_of_death[-1:].isdigit():
                print(message)
                continue
            # date_death = datetime.datetime.strptime(date_of_death, '%d.%m.%Y')
            data_dict['date of death'] = date_of_death
            # data.save_to_list(data_list)
            end = input('Данны сохранены, нажмите Enter для выхода: ')
            break
            #

    @staticmethod
    def load():
        data.loading_files()

    @staticmethod
    def search():
        with open('jsontest.json', encoding='utf-8') as f:
            file_reader = json.load(f)
            print(file_reader)
        # tweets = []
        # for line in open('jsontest.json', 'r'):
        #     tweets.append(json.loads(line))


#
#
