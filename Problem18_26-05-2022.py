# Write a program that accepts sequence of lines as input and prints the lines after making
# all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT


l1=[]
while True:
    s = input()
    if s:
        l1.append(s.upper())
    else:
        break
for sentence in l1:
    print(sentence)

# Write a program that accepts a sequence of whitespace separated words as input and
# prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

l2 = input("Please enter the words\n").split()
print(" ".join(sorted(set(l2))))