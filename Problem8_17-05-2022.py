#Write a Python program which accepts a sequence of comma-separated numbers from user
# and generate a list and a tuple with those numbers.

#My Solution
l2 = list(input("Please enter comma seperated numbers\n").split(","))
t2=tuple(l2)
print(l2)
print(t2)

#Proposed Solution
values = input("Input some comma seprated numbers : \n")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)
