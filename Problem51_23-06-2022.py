# Write a program to compute:
#
# f(n)=f(n-1)+100 when n>0
# and f(0)=1

# f(1) = 101
# f(2) = 201
# f(3) = 301
# f(4) = 401
# f(5) = 501

def f(n):
    if n == 0:
        return 1
    return f(n-1) + 100

n = int(input("please enter value of n\n"))

res = f(n)
print(res)



