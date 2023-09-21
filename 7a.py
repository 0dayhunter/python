class Shape:
    def __init__(self):
        self.area = 0

class Circle(Shape):
    def __init__(self, r):
        super().__init__()
        self.radius = r
        self.area = 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, l, b):
        super().__init__()
        self.length = l
        self.breadth = b
        self.area = self.length * self.breadth

class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        s = (self.a + self.b + self.c) / 2
        self.area = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

if __name__ == '__main__':
    print("Enter your choice to compute area of 1. Circle, 2. Rectangle, 3. Triangle")
    ch = int(input())

    if ch == 1:
        r = int(input("Enter radius of circle: "))
        c = Circle(r)
        print("The area of circle is", c.area)

    elif ch == 2:
        l = int(input("Enter length of rectangle: "))
        b = int(input("Enter breadth of rectangle: "))
        r = Rectangle(l, b)
        print("The area of rectangle is", r.area)

    elif ch == 3:
        a = int(input("Enter side a of triangle: "))
        b = int(input("Enter side b of triangle: "))
        c = int(input("Enter side c of triangle: "))
        t = Triangle(a, b, c)
        print("The area of triangle is", t.area)
