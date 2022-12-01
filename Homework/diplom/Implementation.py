# реализация данных: методы загрузки, сохранения, ввода и поиска данных введенных оператором
import json

import openpyxl

from openpyxl import load_workbook
import csv
import json


class Main:
    SAVE_FILE = 'Data.xlsx'
    LOAD_FILE = 'Data.xlsx'
    SEARCH_FILE = 'Data.xlsx'

    @staticmethod
    def save_file(self):
        data_input = dict(self)
        data_input_values = ([*data_input.values()])
        with open('data.csv', 'a', newline="") as f_obj:
            dict_writer = csv.writer(f_obj, delimiter=";")
            dict_writer.writerow(data_input_values)

    @staticmethod
    def loading_files():
        with open('data.csv') as reader:
            file_reader = csv.reader(reader, delimiter=";")
            for item in file_reader:
                print(item)

    @classmethod
    def search_file(cls):
        wb = openpyxl.Workbook
        wb = openpyxl.load_workbook(cls.SEARCH_FILE)
        sheet = wb.active

    @staticmethod
    def save_to_list(self):
        # try:
        #     data = json.load(open('jsontest.json'))
        # except:
        #     data = [self]
        data = self
        with open('jsontest.json', 'a') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

        # with open('jsontest.json', 'w', encoding='UTF-8') as f:
        #     f.write(json.dumps(person_data, ensure_ascii=False))
        # # for item in person_data:

# data = Main()
#
# data.loading_files()
# data.save_file()


# class Main:
#     @staticmethod
#     def save_file(self):
#         data_input = self.data_input
#         with open('Data.csv', 'w') as f:
#             fieldnames = data_input[0].keys()
#             writer = csv.DictWriter(f, fieldnames=fieldnames)
#             writer.writeheader()
#
