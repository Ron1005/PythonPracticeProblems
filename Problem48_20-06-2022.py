#Define a custom exception class which takes a string message as attribute.

class newexception(Exception):
    def __init__(self,attribute):
        self.attribute = attribute
        print(self.attribute)


ne = newexception("some attribute")

# Assuming that we have some email addresses in the "username@companyname.com" format,
# please write program to print the user name of a given email address.
# Both user names and company names are composed of letters only.

username , notusername = list(input().split("@"))
companyname = str(notusername).split(".")[0]

print(username)
print(companyname)