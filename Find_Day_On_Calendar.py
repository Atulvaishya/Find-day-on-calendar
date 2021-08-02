import calendar

print("---*---*---WELCOME IN SMART CALENDAR---*---*---")

print("This calendar is written in python programming")

year = int(input("Enter Year : "))

month = int(input("Enter Month : "))

day = int(input("Enter Day : "))

day = calendar.weekday(year,month,day)

weekday = calendar.day_name[day]

print("Your Day is : ",weekday)