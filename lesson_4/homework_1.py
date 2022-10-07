# 1. Создать 3 переменные с одинаковыми данными (и одинаковым типом) и с одинаковыми идентификаторами (не присваивая значения переменных друг другу)
# 2. Создать 2 переменные с одинаковыми данными (и одинаковым типом) и с разными
# идентификаторами
# 3. Поменять их типы так, чтобы у 1-х трёх стали разные идентификаторы, но при этом остались
# одинаковые данные (и одинаковым типом), а у 2-х последних стали одинаковые идентификаторы и остались одинаковые
# данные.

variable_1 = "One"
variable_2 = "One"
variable_3 = "One"

print(variable_2 == variable_3)
print(variable_1 is variable_2)
#print(type(variable_1), type(variable_2), type(variable_3))
#print(id(variable_1), id(variable_2), id(variable_3))

print("-" * 20)

variable_4 = {"Two", 2, "Four"}
variable_5 = {"Two", 2, "Four"}

print(variable_4 == variable_5)
print(variable_4 is variable_5)
#print(type(variable_4), type(variable_5))
#print(id(variable_4), id(variable_5))

print("-" * 20)

variable_1 = set("One")
variable_2 = set("One")
variable_3 = set("One")

print(variable_1 == variable_3)
print(variable_1 is variable_2)

print("-" * 20)

variable_4 = frozenset
variable_5 = frozenset

print(variable_4 is variable_5)
print(variable_4 == variable_5)