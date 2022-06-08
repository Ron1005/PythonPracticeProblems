# In a list of comma seperated strings check and print all the strings which are palindrome

#Example:
#list = abba,bba,abbbba
#output =  abba,abbbba


l1= input("Enter list of strings\n").split(",")
res=[]
for word in l1:
    if word == word[::-1]:
        res.append(word)

print(",".join(res))