class Rectangle():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def square(self):
        return float(self.a * self.b)


class Triangle():

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def square(self):
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c))**0.5


class Round():

    def __init__(self, a):
        self.a = a

    def square(self):
        p = 3.14
        return p * self.a ** 2


form = input()

if form == "треугольник":
    a = int(input())
    b = int(input())
    c = int(input())
    figure = Triangle(a, b, c)
    print(figure.square())
elif form == "прямоугольник":
    a = int(input())
    b = int(input())
    figure = Rectangle(a, b)
    print(figure.square())
elif form == "круг":
    a = int(input())
    figure = Round(a)
    print(figure.square())
