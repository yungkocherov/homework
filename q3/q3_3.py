import math


class Figure:
    def area(self, a, b):
        return a * b

    def p(self, a, b):
        return (a + b) * 2


class Circle(Figure):
    def f1(self, r):
        a = r
        b = r * math.pi
        return Figure.area(self, a, b)

    def f2(self, r):
        b = r
        return Figure.p(self, 0, b)


class rectangle(Figure):
    def f1(self, h, w):
        a = h
        b = w

        return Figure.area(self, a, b)

    def f2(self, h, w):
        a = h
        b = w

        return Figure.p(self, a, b)


print("Circle")
r = float(input("enter radius:"))

print("area=", Circle().f1(r))
print("perimeter=", Circle().f2(r))

print("rectangle")
h = float(input("enter height :"))
w = float(input("enter width:"))
print("area=", rectangle().f1(h,w))
print("perimeter=", rectangle().f2(h,w))
