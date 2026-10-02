year = int(input("Enter the year: "))
day = int(input("Enter the day number: "))

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

if leap_year(year):
    days[1] = 29

month = 0

while day > days[month]:
    day = day - days[month]
    month = month + 1

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

def ordinal(day):
    if 10 < day % 100 < 14:
        return str(day) + "th"

    if day % 10 == 1:
        return str(day) + "st"
    elif day % 10 == 2:
        return str(day) + "nd"
    elif day % 10 == 3:
        return str(day) + "rd"
    else:
        return str(day) + "th"

print(months[month], ordinal(day))