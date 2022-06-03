#Define a function that can convert a integer into a string and print it in console.


def convertinttostr(num):
    print(type(str(num)))

convertinttostr(3)

# Define a function that can accept two strings as input and print the string with maximum length in console.
# If two strings have the same length, then the function should print all strings line by line.

s1 = input("Enter First String\n")
s2 = input("Enter Second String\n")

if len(s1)>len(s2):
    print(s1)
elif len(s2)>len(s1):
    print(s2)
else:
    print(s1)
    print(s2)

# Define a function which can print a dictionary where the keys
# are numbers between 1 and 3 (both included) and the values are square of keys.

def printdict():
    d1={n:n**2 for n in range(1,4)}
    print(d1)

printdict()

