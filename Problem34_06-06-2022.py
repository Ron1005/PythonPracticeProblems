# Define a function which can generate
# and print a list where the values are square of numbers between 1 and 20 (both included).

def generatelist():
    print([x*x for x in range(1,21)])

generatelist()

# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print the first 5 elements and last 5 elements in the list.

def generatelist2():
    l1=[x*x for x in range(1,21)]
    print(l1[:5])
    print(l1[-5:])

generatelist2()