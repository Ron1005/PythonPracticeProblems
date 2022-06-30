# Question:
#
# Please write a program using generator to print the even numbers
# between 0 and n in comma separated form while n is input by console.

def generateEvenNumbers(n):
        i=0
        while i<=n:
            if i%2==0:
                yield i
            i+=1

n = int(input("Please enter the number\n"))

res=[]
for x in generateEvenNumbers(n):
    res.append(str(x))

print(",".join(res))