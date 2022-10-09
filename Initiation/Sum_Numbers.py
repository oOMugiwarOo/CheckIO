import re


def sum_numbers(text: str) -> int:
    c = 0
    for i in text.split(' '):
        if i.isdigit():
            c += 1
    if c > 0:
        digit = re.findall(r'\d+', text)
        c = 0
        for i in digit:
            c += int(i)
        return c
    else:
        return 0


print("Example:")
print(sum_numbers("hi"))

assert sum_numbers("hi") == 0
assert sum_numbers("who is 1st here") == 0
assert sum_numbers("my numbers is 2") == 2
assert (
    sum_numbers(
        "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
    )
    == 3755
)
assert sum_numbers("5 plus 6 is") == 11
assert sum_numbers("") == 0