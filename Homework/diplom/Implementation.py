import csv


class Main:

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
                print(f'{item[0]} {item[1]} {item[2]}, {item[3]} лет. Родился: {item[4]}, пол: {item[5]}, статус: {item[6]}')

