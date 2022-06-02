# Use a list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,9,25,49,81

l1 = [ str(int(x)*int(x)) for x in input("Please enter comma separated list\n").split(",") if int(x)%2!=0]

print(",".join(l1))


#Write a method which can calculate square value of number

num = int(input("Enter the number\n"))

print(num**2)
