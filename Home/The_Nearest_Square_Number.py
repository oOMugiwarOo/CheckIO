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


# n = 998500
# x = 0
# a = []
# while True:
#     # if math.sqrt(x) % 2 == 0 or math.sqrt(x) % 3 == 0 or math.sqrt(x) % 5 == 0:
#     if math.sqrt(x) == int(math.sqrt(x)):
#         a.append(x)
#         if math.sqrt(n) < math.sqrt(x):
#             break
#         x += 1
#     else:
#         x += 1
# counter = n
# print(a)
# for i in a:
#     c = n - i
#     if abs(c) < counter:
#         counter = c
# if counter < 0:
#     print(n+abs(counter))
# else:
#     print(n-abs(counter))
#
# print((math.sqrt(998400) == int(math.sqrt(998400))))


