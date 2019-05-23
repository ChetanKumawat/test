import calendar

cal = calendar.Calendar(firstweekday=0)
count=0
for x in cal.iterweekdays():
    if count==0:
        print("1) iterweekdays() method return all days of week : ",x)
    else:
        print(" "*51,x)
    count=count=1



cal = calendar.Calendar()
count=0
for x in cal.itermonthdates(2016,5):
    if count==0:
        print("\n2) itermonthdates() return iterator that will return all days for the month in year and all days before start the month or after end of the month that are required to get a complete week : ",x)
    else:
        print(" "*189,x)
    count=count=1



cal = calendar.Calendar()
count=0
for x in cal.itermonthdays(2019,6):
    if count==0:
        print("\n3) itermonthdays() return iterator that will return all days for the month number : ",x)
    else:
        print(" "*82,x)
    count=count+1



cal =calendar.Calendar()
count=0
for x in cal.itermonthdays2(2016,5):
    if count==0:
        print("\n4) itermonthdays2() return that will be return tuples consisting of a day number and week day number : ",x)
    else:
        print(" "*103,x)
    count=count+1


