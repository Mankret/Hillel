# Для рассмотренного на уроке класса Circle реализовать метод производящий вычитание двух окружностей,
# вычитание радиусов произвести по модулю. Если вычитаются две окружности с одинаковым значением радиуса,
# то результатом вычитания будет точка класса Point.
import math


class Point():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)


class Circle(Point):

    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __str__(self):
        return super().__str__()[:-1] + f', radius = {self.radius})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        radius = self.radius + other.radius
        return Circle(radius, x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        radius = abs(self.radius - other.radius)
        if radius == 0:
            return Point(x, y)
        return Circle(radius, x, y)

    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius)

    def circumference(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius ** 2)


circle1 = Circle(4, 4, 4)
circle2 = Circle(4, 2, 2)

result = circle1 -circle2

print(type(result), result, sep='\n')
print('*' * 30)
circle3 = Circle(8, 4, 6)
circle4 = Circle(10, 12, 14)

result_2 = circle3 - circle4
print(type(result_2), result_2, sep='\n')