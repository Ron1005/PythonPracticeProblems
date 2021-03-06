# Write a program which accepts a sequence of comma-separated numbers from console and generate
# a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

l1 = list(input("Please enter comma separated numbers\n").split(","))
t1 = tuple(l1)

print(l1)
print(t1)


# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
class Demo:
    def getString(self):
        self.s = input("Enter the String\n")

    def printString(self):
        print(self.s.upper())

def TestFunction():
    d1 = Demo()
    d1.getString()
    d1.printString()

TestFunction()

# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

from math import sqrt
C = 50
H = 30
l1 = list(map(int,input("Please enter comma separated numbers\n").split(",")))
l2=[]
for x in l1:
    l2.append(str(int(sqrt((2*C*x)/H))))

print(",".join(l2))