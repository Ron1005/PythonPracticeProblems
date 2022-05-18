#  Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

exam_st_date = (11, 12, 2014)
print(str(exam_st_date[0])+" / "+str(exam_st_date[1])+" / "+str(exam_st_date[2]))


# Write a Python program to display the first and last colors from the following list. Go to the editor
# color_list = ["Red","Green","White" ,"Black"]

color_list = ["Red","Green","White" ,"Black"]
print(color_list[0])
print(color_list[-1])

# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5
# Expected Result : 615

n = int(input("Enter value for n\n"))
print("Result of n + nn + nnn is {}:".format((n)+(n*10 + n)+(n*100 + n*10 + n)))