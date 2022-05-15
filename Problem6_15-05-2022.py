#Write a Python program which accepts the radius of a circle from the user and compute the area

#My Solution
from math import pi
r=float(input())
area = pi*r**2
print("Area of the circle is {:.2f}".format(area))

#Proposed Solution
r1 = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r1) + " is: " + str(pi * r1**2))


