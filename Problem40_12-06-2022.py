#Print Name 5 time using Recursion

name = input("Enter your name\n")

def printname(name,count):
    if count==5:
        return
    print(name)
    printname(name,count+1)

printname(name,0)

#Print values from 1 to N using Recusrion
N = int(input("Enter value of N\n"))

def printvaluefrom1toN(num):
    if num == N + 1:
        return
    if num == N:
        print(num)
    else:
        print(num,end=",")
    printvaluefrom1toN(num+1)

printvaluefrom1toN(1)

#Print value from N to 1 using Recusrion


def printvaluefromNto1(num):
    if num == 0:
        return
    if num == 1:
        print(num)
    else:
        print(num,end=",")
    printvaluefromNto1(num-1)

printvaluefromNto1(N)

