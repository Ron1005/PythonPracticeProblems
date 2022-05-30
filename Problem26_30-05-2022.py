# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

s = input("Enter the sentence\n")
letters=0
digits=0
for x in s:
    if x.isdigit():
        digits+=1
    elif x.isalpha():
        letters += 1

print("LETTERS ",letters)
print("DIGITS ",digits)

# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

s1=input("\nEnter the 2nd sentence\n")
uppercase=0
lowercase=0
for x in s1:
    if x.isalpha() and x.isupper():
        uppercase+=1
    elif x.isalpha() and x.islower():
        lowercase+=1

print("UPPERCASE ",uppercase)
print("LOWERCASE ",lowercase)

# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

num = input()
sum1=0
tempnum=num
for x in range(0,4):
    sum1 = sum1 + int(tempnum)
    tempnum=tempnum+num
print(sum1)