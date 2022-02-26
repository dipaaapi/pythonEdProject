import calendar
import datetime as dt

yy = 1989
mm = 1
dd = 28
datetoday = dt.date.today()
datebirth = dt.date(yy, mm, dd)
age = datetoday.year - datebirth.year

if age > 18:
    print("matanda ka na")
else:
    print("bagets ka pa")

print(calendar.month(yy, mm, dd))
print("Today it's " + str(datetoday))
print(datebirth)
print(datebirth.year)
print(datetoday.year)
print(datetoday.year - datebirth.year)
print(age)

