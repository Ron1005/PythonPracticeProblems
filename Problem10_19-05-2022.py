#Write a Python program to print the calendar of a given month and year.
import calendar

y = int(input("Enter year\n"))
m = int(input("Enter Month\n"))

calendarlist = calendar.monthcalendar(y,m)

print("Mon\tTue\tWed\tThu\tFri\tSat\tSun")
for week in calendarlist:
    weeks=""
    for day in week:
        if day == 0:
            weeks+="-" + "\t"
        else:
            weeks += str(day) + "\t"
    print(weeks,end="\n")

#Write a Python program to calculate number of days between two dates.

from datetime import date
t1 = tuple(map(int,input("Enter date 1 in yyyy-mm-dd format\n").split("-")))
t2 = tuple(map(int,input("Enter date 2 in yyyy-mm-dd format\n").split("-")))
d1 = date(t1[0],t1[1],t1[2])
d2 = date(t2[0],t2[1],t2[2])

print(abs((d2-d1).days))


