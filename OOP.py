import math


class Triangle(object):
    dot0: list
    line: int

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
    obj1 = triangle_square.square()
    obj2 = rectangle_square.square()

    if obj1 > obj2:
        s = obj1 - obj2
        print(f"Площадь треугольника > площади прямоугольника на {s}")
    else:
        s = obj2 - obj1
        print(f"Площадь треугольника < площади прямоугольника на {s}")


def intersection(t1, t2):
    T_dot0 = t1.dot0
    R_dot0 = t2.dot0
    T_h = t1.line * (math.sqrt(3) / 2)
    array1 = [T_dot0[0], T_h, t1.line, T_dot0[1]]
    array2 = [R_dot0[0], t2.h, t2.w, R_dot0[1]]
    x12 = T_dot0[0] + t1.line
    x22 = R_dot0[0] + t2.w
    x1 = [T_dot0[0], x12]
    x2 = [R_dot0[0], x22]
    y12 = T_dot0[1] + T_h
    y22 = R_dot0[1] + t2.h
    y1 = y12
    y2 = [R_dot0[1], y22]
    if max(x1) < min(x2) or min(x1) > max(x2) or max(y1) < min(y2) or min(y1) > max(y2):
        print("Не пересекается")
    else:
        print("Пересекается")


Rectangle_1 = Rectangle((5, 5), 30, 10)
Triangle_1 = Triangle((0, 0), 10)
print("Площадь прямоугольника")
print(Rectangle_1.square())
print("Площадь треугольника")
print(Triangle_1.square())
compare(Triangle_1, Rectangle_1)
intersection(Triangle_1, Rectangle_1)
