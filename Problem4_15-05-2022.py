# Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

from datetime import datetime
#My Solution
print(datetime.now())

#Proposed Solution
now = datetime.now()
print ("Current date and time : ")
#strftime function is used to format datetime in required format
#%Y - Year, %m - Month , %d - Day , %H - Hours , %M - Minutes , %S - Seconds
print (now.strftime("%Y-%m-%d %H:%M:%S"))


