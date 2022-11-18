import math

class Triangle(object):

    dot1: list
    dot2: list
    dot3: list

    def __init__(self, dot1, dot2, dot3):
        self.dot1 = dot1
        self.dot2 = dot2
        self.dot3 = dot3

    # Площадь через 3 стороны треугольника
    def Square(self):
        def edgelength(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2)
        self.d1d2 = edgelength(self.dot1, self.dot2)
        self.d2d3 = edgelength(self.dot2, self.dot3)
        self.d3d1 = edgelength(self.dot3, self.dot1)
        halfperimeter = (self.d1d2 + self.d2d3 + self.d3d1) / 2
        return math.sqrt(halfperimeter * (halfperimeter - self.d1d2) * (halfperimeter - self.d2d3) * (halfperimeter - self.d3d1))

class Rectangle(object):

    w: int
    h: int
    dot0: list

    def __init__(self, dot0, w, h):
        self.dot0 = dot0
        self.w = w
        self.h = h

    def Square(self):
        return self.w * self.h

#class Functions():
def Compare(triangle_square, rectangle_square):
    obj1 = triangle_square
    obj2 = rectangle_square
    if(obj1 > obj2):
        s = obj1 - obj2
        print("Площадь треугольника > площади прямоугольника")
    else:
        s = obj2 - obj1
        print("Площадь треугольника < площади прямоугольника")


Rectangle_1 = Rectangle((1,1), 20, 10)
Triangle_1 = Triangle((3, 2), (6, 7), (0, 12))
print(Rectangle_1.Square())
print(Triangle_1.Square())
Compare(Triangle_1.Square(), Rectangle_1.Square())
