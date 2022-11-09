# Создать 2 класса truck и car, которые являются наследниками класса auto из предыдущего домашнего задания.
# Класс truck имеет дополнительный обязательный атрибут max_load.
# Переопределённый метод move, перед появлением надписи «move» выводит надпись «attention», его реализацию сделать
# при помощи оператора super.
# А так же дополнительный метод load. При его вызове происходит пауза 1 сек., затем выдаётся сообщение «load» и снова
# пауза 1 сек.
# Класс car имеет дополнительный обязательный атрибут max_speed и при вызове
# метода move, после появления надписи «move» должна появиться надпись
# «max speed is <max_speed>». Вместо <max_speed> должно выводится значение обязательного атрибума max_speed.
# Создать по 2 объекта для каждого из классов truck и car, проверить все их методы и атрибуты.
from homework_21 import Auto
import time


class Truck(Auto):
    max_load = True
    weight = '8500 kg'

    def __init__(self, brand, age, mark, max_load):
        super().__init__(brand, age, mark)
        self.max_load = max_load

    def move(self):
        print("Attention")
        super().move()

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)


class Car(Auto):
    max_speed = True
    weight = '2000 kg'

    def __init__(self, brand, age, mark, max_speed):
        super().__init__(brand, age, mark)
        self.max_speed = max_speed

    def move(self):
        super(Car, self).move()
        print(f"Max speed is {self.max_speed}")


print("!!!testing class Truck")

test_truck = Truck('brands', 2011, 'Scania', 2314)
print(f"Brand is {test_truck.brand}")
test_truck.move()
test_truck.load()
print(f"color is {test_truck.color}, weight this truck is {test_truck.weight}")
print(test_truck.mark)
print(f"Age  this truck is {test_truck.age}")
# test_truck.birthday()
test_truck.stop()

print("*" * 50)
print("!!!testing class Car")
mcar = Car('bb', 2009, 'BMW', 266)
print(f"Brand is {mcar.brand}")
print(f"Color is {mcar.color}, and weight is {mcar.weight}")
print(f"Mark is {mcar.mark}")
print(f"Age  this car is {mcar.age}")
mcar.move()
# mcar.birthday()
mcar.stop()
