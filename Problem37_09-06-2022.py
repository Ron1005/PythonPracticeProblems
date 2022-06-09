# Write a program which can filter even numbers in a list by using filter function.
# The list is: [1,2,3,4,5,6,7,8,9,10].

l1 = [1,2,3,4,5,6,7,8,9,10]

l2 = list(filter(lambda x:x%2==0,l1))

print(l2)

#Write a program which can map() to make a list whose
# elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

l3 = list(map(lambda x:x*x,l1))

print(l3)

# Write a program which can map() and filter() to make a
# list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

l4= list(map(lambda x:x*x,filter(lambda x:x%2==0,l1)))
print(l4)