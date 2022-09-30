from datetime import datetime, date, time


def friday(day: str) -> int:
    year = int(day.split('.')[2])
    month = int(day.split('.')[1])
    day = int(day.split('.')[0])
    day_of_stand = date(year, month, day)

    if date.weekday(day_of_stand) == 4:
        return 0

    elif date.weekday(day_of_stand) < 4:
        return 4 - date.weekday(day_of_stand)
    else:
        if date.weekday(day_of_stand) == 5:
            return 6
        elif date.weekday(day_of_stand) == 6:
            return 5

print("Example:")
print(friday("23.04.2018"))

assert friday("12.04.2018") == 1
assert friday("01.01.1999") == 0

# a = "01.01.1999"
# year = int(a.split('.')[2])
# month = int(a.split('.')[1])
# day = int(a.split('.')[0])
#
# d = date(2022, 9, 26)
# d1 = date(2018, 4, 12)
# d2 = date(year, month, day)
#
# if date.weekday(d2) < 4:
#     print(4-date.weekday(d2))


# print(date.weekday(d))
# print(date.weekday(d1))
# print(date.weekday(d2))
# c = date.weekday(d2)
# print(type(c))

