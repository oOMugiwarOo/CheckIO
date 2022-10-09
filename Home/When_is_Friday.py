from datetime import date


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
