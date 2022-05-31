# Use a list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9

l1 = list(map(int,input("please enter the input list\n").split(",")))
res= [ str(x) for x in l1 if x%2!=0]

print(",".join(res))


# Write a program that computes the net amount of a bank account based a transaction log from console input.
# The transaction log format is shown as following:
# D 100
# W 200
#
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

sum0=0
while True:
    s=input()
    if s:
       if s[0] == 'D':
           sum0=sum0+int(s[2:])
       elif s[0] == 'W':
           sum0 = sum0 - int(s[2:])
    else:
        break
        
print(sum0)
