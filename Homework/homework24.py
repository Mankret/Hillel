# Создать свой класс String на базе стандартного класса str.
#
# В нём необходимо:
#
# переопределить стандартный метод отвечающий за сложение
# написать отсутствующий в классе str метод отвечающий за вычитание
#
#
# Принцип работы сложения в новом классе String: объект типа String можно складывать как друг с другом, так и с любым
# другим типом, который может быть приведён к строковому типу. "Под капотом" оба операнда приводятся к строковому
# типу и происходит конкатенация двух строк.
#
#
# String('New') + String(890)    ->    'New890'
# String(1234) + 5678    ->    12345678
# String('New') + 'castle'    ->    'Newcastle'
# String('New') + 77    ->    'New77'
# String('New') + True    ->    'NewTrue'
# String('New') + ['s', ' ', 23]    ->    "New['s', ' ', 23]"
# String('New') + None    ->    'NewNone'


# Принцип работы вычитания в новом классе String: из объекта типа String
# можно вычесть значение любого другого типа, которое может быть приведёно к строковому типу. "Под капотом" оба
# операнда приводятся к строковому типу и затем из первого операнда убирается первое вхождение второго операнда,
# если таковое имеется. Если в первом операнде не находится значение второго операнда, то результатом вычитания будет
# первый операнд без изменений. Примеры выполнения:
#

# String('New bala7nce') - 7    ->    'New balance'
# String('New balance') - 'bal'    ->    'New ance'
# String('New balance') - 'Bal'    ->    'New balance'
# String('pineapple apple pine') - 'apple'    ->    'pine apple pine'
# String('New balance') - 'apple'    ->    'New balance'
# String('NoneType') - None    ->    'Type'
# String(55678345672) - 7    ->    '5568345672'
# #
# #



class String(str):

    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        x = str(self) + str(other)

        return String(x)

    def __sub__(self, other):
        x = str(self).replace(str(other), '', 1)
        return String(x)


print('Testing the subtraction method')

string5 = String('New bala7nce')

print(string5 - 7)
print(String('New balance') - 'bal')
print(String('New balance') - 'Bal')
print(String('pineapple apple pine') - 'apple')
print(String('New balance') - 'apple')
print(String('NoneType') - None)
print(String(55678345672) - 7)
print(type(string5 - 7))
print(type(String('New balance') - 'bal'))
print(type(String('New balance') - 'Bal'))
print(type(String('pineapple apple pine') - 'apple'))
print(type(String('New balance') - 'apple'))
print(type(String('NoneType') - None))
print(type(String(55678345672) - 7))

#
# print("Testing the assignment method")

# string1 = String(1234)
# string2 = String(['s', ' ', 23])
# string3 = String('New')
#
# result = string1 + string2
# print(result)
# print(string3 + 'castle')
# print(string1 + 5678)
# print(string3 + 77)
# print(string3 + True)
# print(string3 + None)
# print('/|||' * 50)
# print(type(result))
# print(type(string3 + 'castle'))
# print(type(string1 + 5678))
# print(type(string3 + 77))
# print(type(string3 + True))
# print(type(string3 + None))
