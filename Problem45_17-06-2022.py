# Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.


class Shape:

    def getarea(self):
        return 0

class Square(Shape):
    def __init__(self,lenth):
        self.length = lenth

    def getarea(self):
        return self.length**2



S1 = Square(10)
print(S1.getarea())

#Please raise a RuntimeError exception.
try:
    raise RuntimeError("Some Exception")
except Exception as ex:
    print("Exception occurred",ex)

#Write a function to compute 5/0 and use try/except to catch the exceptions.

try:
    print(5/0)
except Exception as ex:
    print("Exception occurred",ex)

