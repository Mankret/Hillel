# Прочитать сохранённый json-файл из задания №17 и записать данные на диск в csv-файл, первой строкой которого
# озаглавив каждый столбец и добавив новый столбец “телефон”.

import csv
import json

with open('jsontest.json', 'r') as f:
    data = json.load(f)

additional_data = [['Id', 'Name', 'Age', 'Phone']]


with open('data_csv.csv', 'w', newline="") as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerows(additional_data)

    for line in (data.items()):
        writer.writerow(line)
