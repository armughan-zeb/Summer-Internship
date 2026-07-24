class Shape:
    def area(self):
        print("Area of Shape")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area of Circle =", 3.14 * self.radius * self.radius)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area of Rectangle =", self.length * self.width)

c = Circle(5)
r = Rectangle(4, 6)

c.area()
r.area()