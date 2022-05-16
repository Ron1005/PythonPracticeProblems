#Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them

#My Solution
fullname = list(map(lambda x: x.strip() + " ",input("please type your complete name\n").split()))

fullname.reverse()

nametoprint = "".join(fullname)

# for name in fullname:
#     nametoprint+=name + " "

print(nametoprint)

#Proposed Solution

fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello " + lname + " " + fname)




