#Write a program which accepts a sequence of words separated by whitespace as
# input to print the words composed of digits only

l1 = list(filter(lambda x : str(x).isdigit(),input("Please enter the sequence of words\n").split()))

print(l1)

