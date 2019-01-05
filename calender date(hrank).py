from datetime import date
import calendar
import datetime

from dateutil.parser import parse
m,d,y = list(map(str,input().split()))
#print(m,d,y)
my_date = str(d + m + y)
v = datetime.datetime.strptime(my_date, "%d%m%Y").date()
week = calendar.day_name[v.weekday()]
lowery = week[1:].lower()
upper = week[0]
#print(lowery,upper)
print(upper+lowery)
