class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return self.a + self.b + self.c


class Rectangle(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_perimeter(self):
        return (self.a + self.b) * 2

Pryam = Rectangle(2, 4)
print(Pryam.get_perimeter())
