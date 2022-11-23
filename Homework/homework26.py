# Создать программу-калькулятор в виде класса и несколько методов, как минимум сложение, вычитание, деление,
# умножение, возведение в степень и извлечение квадратного корня.
# Обернуть каждый метод в блок try/except и сделать обработку нескольких исключений, как минимум деление на 0.
# Создать своё исключение, к примеру возведение в отрицательную степень.
import math


class MyException(BaseException):
    def __init__(self, message):
        self.message = message


class Calcul:
    def __init__(self, x=0):
        self.x = x

    def __add__(self, other):
        try:
            result = self.x + other.x
            return result
        except AttributeError as error:
            print('Wrong attribute', error)
            return self.x
        except TypeError as error:
            print('Wrong type: ', error)
            return self.x, other.x

    def __sub__(self, other):
        try:
            result = self.x - other.x
            return result
        except TypeError as error:
            print('Wrong type', error)
            return self.x, other.x

    def __mul__(self, other):
        try:
            result = self.x * other.x
            return result
        except Exception as error:
            print('Error: ', error)
            return self.x, other.x

    def __floordiv__(self, other):
        try:
            result = self.x // other.x
            return result
        except ZeroDivisionError as error:
            print("Can't division on zero: ", error)
            return self.x, other.x

    def __pow__(self, other):
        try:
            result = self.x ** other.x
            if self.x < 0 or other.x < 0:
                raise MyException('You write negative value')
        except MyException as error:
            print(error)
            return self.x, other.x
        else:
            return result

    def sqrt(self, other):
        try:
            self.x = math.sqrt(other.x)
            return self.x
        except ValueError as error:
            print("Invalid value: ", error)
            return other.x


res0 = Calcul()
res1 = Calcul(5)
res2 = Calcul(2)
# resul = res1 + res2
# print(res1 + res2)
# print(res1 - res2)
# print(res1 * res2)
# print(res1 // res2)
print(res1 ** res2)
#print(res0.sqrt(res2))
