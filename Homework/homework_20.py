# Реализовать код, который выведет следующие наборы данных.
# 1) Прибыль по таблице invoice_items. Сумма по заказу =
# UnitPrice * Quantity (если через sql, то нужно использовать sum). В итоге через функцию print() выводим 1 цифру
# общей прибыли.
# 2) Считаем кол-во повторений FirstName в таблице customers. Через функцию print() выводим имя и
# кол-во его повторений.


import os
import sqlite3

db_pass = os.path.join(os.getcwd(), 'chinook.db')
connection = sqlite3.connect(db_pass)
cur = connection.cursor()

#
# query_sql = '''
#     SELECT sum(UnitPrice * Quantity)
#       FROM invoice_items;
# '''
# rows = cur.execute(query_sql).fetchone()
#
# for row in rows:
#     print("Сумма общей прибыли = ", round(row))
#
#


query_sql = '''
     SELECT FirstName, COUNT(FirstName)
        FROM customers
        GROUP BY FirstName;
 '''
rows = cur.execute(query_sql).fetchall()


for row in rows:
    print("Имя и количество повторов : ", *row)


connection.close()
