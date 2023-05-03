import calendar

date = input("Enter a date: ")
date = date.split("/")
day= calendar.weekday(int(date[2]), int(date[1]), int(date[0]))

if day == 0:
	print("Monday")
elif day == 1:
	print("Tuesday")
elif day == 2:
	print("Wednesday")
elif day == 3:
	print("Thursday")
elif day == 4:
	print("Friday")
elif day == 5:
	print("Saturday")
else:
	print("Wrong output")
