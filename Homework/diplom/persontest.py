import datetime
import json

from Implementation import Main
from datetime import date

data = Main()


class CalculAge:
    @staticmethod
    def agecalc(self):
        today = datetime.datetime.now()
        birth = self
        temp = today - birth
        age = round(temp.days / 365.25)
        return age

    @staticmethod
    def agedeath(self, other):
        death = self
        birth = other
        temp = death - birth
        age = round(temp.days / 365.25)
        return age


calcul = CalculAge()

my_list = []


class Person:

    @staticmethod
    def recording():

        while True:
            today = datetime.datetime.now()
            data_person = []
            message = 'Вы ввели не корректные данные'
            data_dict = {}
            data_new = {}
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

            date_of_born = input('Введите дату рождения: ').replace('-', '.').replace('/', '.').replace(' ', '.')
            if not date_of_born[0:].isdigit() and not date_of_born[-1:].isdigit():
                print(message)
                continue
            date_born = datetime.datetime.strptime(date_of_born, '%d.%m.%Y')
            calcul.agecalc(date_born)
            data_dict['age'] = calcul.agecalc(date_born)

            data_dict['date of born'] = date_of_born

            sex = input('Введите пол: ').title()
            if not sex.isalpha():
                print(message)
                continue
            data_dict['sex'] = sex

            date_of_death = input('Введите дату смерти, (н, n): ').replace('-', '.').replace('/', '.').replace(' ', '.')
            if date_of_death.lower() in ('n', 'н'):
                my_list.append(data_dict)
                end = input('Данны сохранены, нажмите Enter для продолжения: ')
                offer = input('Введите (выход, exit, quit, e, q) для выхода: ')
                if offer.lower() in ('выход', 'exit', 'quit', 'e', 'q'):
                    break
            if not date_of_death[0:].isdigit() and not date_of_death[-1:].isdigit():
                print(message)
                continue
            date_death = datetime.datetime.strptime(date_of_death, '%d.%m.%Y')
            calcul.agedeath(date_death, date_born)
            data_dict['age'] = calcul.agedeath(date_death, date_born)

            data_dict['date of death'] = date_of_death
            my_list.append(data_dict)
            end = input('Данны сохранены, нажмите Enter для выхода: ')
            break
            #

    @staticmethod
    def load():
        data.loading_files()

    @staticmethod
    def search():
        while True:
            data_person = my_list
            search = input("Поиск: ")
            for item, dict_new in enumerate(data_person):
                if search in dict_new.values():
                    print(*dict_new.values())
                else:
                    print("Данные отсутствуют")
                break
            break


    @staticmethod
    def save_to_file():
        for item, dict_new in enumerate(my_list):
            data.save_file(dict_new.items())

        print('Данные сохранены')
