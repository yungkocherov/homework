import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def f1(self):
        self.a = math.pi * self.radius * self.radius
        return (self.a)

    def f2(self):
        self.P = 2 * math.pi * self.radius
        return self.P


class rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def f3(self):
        self.a = self.height * self.width
        return (self.a)


print("Circle")
r = float(input("enter radius:"))
t1 = Circle(r)
print("area=",t1.f1())
t2 = Circle(r)
print("perimeter=", t2.f2())

print("rectangle")
h = float(input("enter height :"))
w = float(input("enter width:"))
rect = rectangle(h, w)
print("area=", rect.f3())
