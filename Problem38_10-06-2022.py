# With a given tuple (1,2,3,4,5,6,7,8,9,10),
# write a program to print the first half values in one line and the last half values in one line.

t1 = (1,2,3,4,5,6,7,8,9,10)

print(t1[0:5])
print(t1[5:])

# Write a program to generate and
# print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

t2 = tuple(filter(lambda x:x%2==0,t1))

print(t2)