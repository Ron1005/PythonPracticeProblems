# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

n = int(input("Enter the number n \n"))

sum=0
for x in range(1,n+1):
   # print(x/(x+1))
    sum = sum + (x/(x+1))
    #print(sum)

print("The sum is {}".format(round(sum,2)))