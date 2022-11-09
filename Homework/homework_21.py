# Создать родительский класс auto, у которого есть атрибуты:
# brand, age, cоlor, mark и weight.
# А так же методы: move, birthday и stop.
# Методы move и stop выводят сообщение на экран «move» и «stop»,а birthday увеличивает атрибут age на 1.
# Атрибуты brand, age и mark являются обязательными при объявлении объекта.

class Auto:
    brand = None
    age = None
    color = 'Black'
    mark = None
    weight = '1985 kg'

    def __init__(self, brand, age, mark):
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        print("Move")

    def birthday(self):
        for item in range(1999, self.age + 1):
            print(f"age:  {item}")

    def stop(self):
        print("Stop")


car = Auto("merce", 2018, '221b')
#car.birthday()
# print("Parent Class")
# #car.stop()
# #car.move()
# print(car.color, car.weight, sep='\n')
# #car.birthday()
