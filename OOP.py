import math


class Triangle(object):
    dot0: list

    def __init__(self, dot0=(0, 0), line=1):
        self.dot0 = dot0
        self.line = line

    # Площадь через 3 стороны треугольника
    def square(self):
        halfperimeter = (self.line * 3) / 2
        return math.sqrt(halfperimeter * ((halfperimeter - self.line) * 3))


class Rectangle(object):
    w: int
    h: int
    dot0: list

    def __init__(self, dot0=(0, 0), w=0, h=0):
        self.dot0 = dot0
        self.w = w
        self.h = h

    def square(self):
        return self.w * self.h


def compare(triangle_square, rectangle_square):
    obj1 = triangle_square
    obj2 = rectangle_square

    if obj1 > obj2:
        s = obj1 - obj2
        print("Площадь треугольника > площади прямоугольника")
    else:
        s = obj2 - obj1
        print("Площадь треугольника < площади прямоугольника")


def intersection(t1, t2):
    dot0 = t1.dot0



Rectangle_1 = Rectangle((1, 1), 20, 10)
Triangle_1 = Triangle((0, 0), 10)
print(Rectangle_1.square())
print(Triangle_1.square())
compare(Triangle_1.square(), Rectangle_1.square())
