import datetime

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A")) #Fullform WeekDay
print(x.strftime("%a")) #Shortform WeekDay
print(x.strftime("%w")) #Daycount {0-6} 0=Sunday
print(x.strftime("%d")) #Date [0-31]
print(x.strftime("%b")) #Shortform Monthname
print(x.strftime("%B")) #Fullformform WeekDay
print(x.strftime("%m")) #Month[0-12]


#CREATE OWN DATE-TIME
y = datetime.datetime(2020, 5, 17)

print(y)