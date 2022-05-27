# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input
# and then check whether they are divisible by 5 or not. The numbers that are divisible
# by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
#Note : Use int(binarynum,2) to convert binary number to integer
#Use bin() function to convert integer to binary number

l1 = input("Please enter comma separated binary numbers\n").split(",")
res = [x for x in l1 if int(x,2)%5==0]
print(",".join(res))

# Write a program, which will find all such numbers between 1000 and 3000 (both included) such
# that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def checkevennums(num):
    while num>0:
        d=num%10
        if d%2==0:
            num=int(num/10)
        else:
            return False
    return True

evennums=[]
for num in range(1000,3001):
    if checkevennums(num):
        evennums.append(str(num))

print(",".join(evennums))
