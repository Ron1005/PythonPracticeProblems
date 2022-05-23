# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

l1=[]
for x in range(2000,32001):
    if x%7==0 and x%5!=0:
        l1.append(str(x))
print(",".join(l1))


# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

def findfact(num):
    fact=1
    while num != 0:
        fact = fact * num
        num = num - 1
    return fact

num = int(input("\nEnter the number\n"))
res = findfact(num)

print("Factoril of {} is {}".format(num,res))

# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an
# integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
num = int(input("Enter the number for dictionary\n"))

d1 = {n:n*n for n in range(1,num+1)}
print(d1)