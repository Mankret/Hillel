# Создайте свой произвольный класс и в нём помимо обычных методов и атрибутов создайте несколько статических методов
# и методов класса.
# Продемонстрируйте их работу.


class SomePerson:
    ID = 5647320909

    @classmethod
    def identification(cls):
        return print('Id this person is: ', cls.ID)

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.information = f'{name} {age}'

    @staticmethod
    def company():
        print("This peron work's in Microsoft")


new_person = SomePerson('David', 22)
print(new_person.information)
SomePerson.identification()
SomePerson.company()
