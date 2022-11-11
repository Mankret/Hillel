# Прочитать сохранённый csv-файл из задания №18 и сохранить данные в excel-файл,
# кроме возраста – столбец с этими данными не нужен.


import openpyxl
import csv

book = openpyxl.Workbook()
sheet = book.active

with open('data_csv.csv', encoding='utf_8') as f:
    file_reader = csv.reader(f, delimiter=';')
    data = list()
    name = list(next(file_reader))
    for items in list(file_reader):
        for item in items:
            data.append(item)

print(len(data), data)

name.remove('Age')

sheet['A1'] = name[0]
sheet['B1'] = name[1]
sheet['C1'] = name[2]
sheet['A2'] = data[0]
sheet['A3'] = data[1]
sheet['A4'] = data[2]
sheet['A5'] = data[3]
sheet['A6'] = data[4]
sheet['C2'] = '125-698'
sheet['C3'] = '495-698'
sheet['C4'] = '625-998'
sheet['C5'] = '935-698'
sheet['C6'] = '116-698'
sheet['B2'] = data[5]
sheet['B3'] = data[7]
sheet['B4'] = data[9]
sheet['B5'] = data[11]
sheet['B6'] = data[13]




book.save('Data_xl.xlsx')
book.close()

#     for row_index, row in enumerate(data):
#         for col_index, value in enumerate(row):
#             cell = sheet.cell(row=row_index + 1, column=col_index + 1)
#             cell.value = value
#
