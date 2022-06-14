#
# Check type of following:
# "CodesDope"
# 15
# 16.2
# 9.33333333333333333333


print(type("CodesDope"))
print(type(15))
print(type(16.2))
print(type(9.33333333333333333333))


# Create a class named 'Rectangle' with two data members- length and breadth and
# a method to claculate the area which is 'length*breadth'. The class has three constructors which are :
# 1 - having no parameter - values of both length and breadth are assigned zero.
# 2 - having two numbers as parameters - the two numbers are assigned as length and breadth respectively.
# 3 - having one number as parameter - both length and breadth are assigned that number.
# Now, create objects of the 'Rectangle' class having none, one and two parameters and print their areas.

#Note : We cannot create multiple paramaterised constructors in python like Java , but in Python we can have optional parameters
#in constructors
class Rectangle:

    def __init__(self,length=0,bredth=0):
        self.length = length
        self.bredth = bredth
        if length ==0 and bredth!=0:
            self.length=bredth
        elif bredth==0 and length!=0:
            self.bredth=length

    def findarea(self):
        return self.length*self.bredth

r1 = Rectangle()
print(r1.findarea())
r2= Rectangle(10,20)
print(r2.findarea())
r3 = Rectangle(20)
print(r3.findarea())

