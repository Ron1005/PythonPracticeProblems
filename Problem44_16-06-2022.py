#Define a class named Circle which can be constructed by a radius.
# The Circle class has a method which can compute the area.
from math import pi
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def printarea(self):
        return pi*self.radius*self.radius


c1 = Circle(5)
print("Area of Circle is",round(c1.printarea(),2))

#Define a class named Rectangle which can be constructed by a length and width.
# The Rectangle class has a method which can compute the area.
class Rectangle:
    def __init__(self,length,bredth):
        self.length = length
        self.bredth = bredth

    def printarea(self):
        return self.length*self.bredth


r1 = Rectangle(10,20)
print("Area of Rectangle is",r1.printarea())

