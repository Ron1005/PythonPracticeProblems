#Write a Python program to get the volume of a sphere with radius 6
from math import pi
r = int(input("Please enter radius of the sphere\n"))
area = (4/3)*pi*r**3
print("Volume of Sphere is : {:.2f}".format(area))

# Write a Python program to calculate the sum of three given numbers, if the values are equal then
# return three times of their sum.
from functools import reduce
listofnumbers = list(map(int,input("Please enter 3 comma separated Numbers\n").split(",")))

print("sum of three numbers is :",reduce(lambda a,b : a+b,listofnumbers))

#Write a Python program to count the number 4 in a given list.

l1 = list(map(int,input("Please enter comma separated Numbers\n").split(",")))

print("Number of times 4 appears is:",l1.count(4))

