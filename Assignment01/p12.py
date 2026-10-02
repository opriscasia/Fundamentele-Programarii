year=int(input ("Please enter the year: "))
month=int(input ("Please enter the month: "))
day=int(input ("Please enter the day: "))

age=0

def leap_year(year):
    if year%400==0:
        return True
    if year%4==0 and year%100!=0:
        return True
    return False

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for year1 in range(year,2026):
    if leap_year(year1):
        age=age+1

age = age + (2026-year) * 365

for month1 in range(month-1,9):
    age = age + days[month1]

if month >= 10:
    for month1 in range(10,month):
        age = age - days[month1]

#daca per
if leap_year(year) and month >= 3:
    age= age - 1

age = age + 2 - day

# The age of a person in number of days up to october 2nd 2026
print("Your age is \033[1;35m" + str(age) + "\033[0m days")