import math


def nearest_square(num: int) -> int:
    x = 0
    a = []
    while True:
        if math.sqrt(x) == int(math.sqrt(x)):
            a.append(x)
            if math.sqrt(num) < math.sqrt(x):
                break
            x += 1
        else:
            x += 1
    counter = num
    for i in a:
        c = num - i
        if abs(c) < counter:
            counter = c
    if counter < 0:
        return num + abs(counter)
    else:
        return num - abs(counter)


print("Example:")
print(nearest_square(8))

assert nearest_square(8) == 9
assert nearest_square(13) == 16
assert nearest_square(29) == 25
assert nearest_square(998500) == 998001
