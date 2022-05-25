# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

a,b = list(map(int,input("Please enter two numbers\n").split(",")))
res=[]
for x in range(a):
    l1=[]
    for y in range(b):
        l1.append(x*y)
    res.append(l1)

print(res)

# Write a program that accepts a comma separated sequence of words as input and prints the words in a
# comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

words = input("Please enter the comma separated words").split(",")

words.sort()
print(",".join(words))
