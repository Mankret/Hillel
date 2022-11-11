# Прочитать сохранённый json-файл из задания №17 и записать данные на диск в csv-файл, первой строкой которого
# озаглавив каждый столбец и добавив новый столбец “телефон”.

import csv
import json

with open('jsontest.json', encoding="utf-8") as f:
    data = json.load(f)

    id_data = zip([*data.values()])
    iq_data = zip([*data.keys()])
fieldnames = [["Id", "Name", "Age", "Phone"]]
# phone = [["111-222"], ["333-444"], ["555-666"], ["777-888"], ["999-111"]]

with open("data_csv.csv", "w", newline="") as f:
    dict_writer = csv.writer(f, delimiter=";")
    dict_writer.writerows(fieldnames)
    dict_writer.writerows(iq_data)
    # dict_writer.writerows(iq_data)
    for item in iq_data:
        dict_writer.writerows(item)

    for items in id_data:
        dict_writer.writerows(items)
