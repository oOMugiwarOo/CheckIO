def checkio(number: int) -> int:
    result = 1
    for i in str(number):
        if int(i) == 0:
            continue
        else:
            result *= int(i)
    return result


print("Example:")
print(checkio(123405))

assert checkio(123405) == 120
assert checkio(999) == 729
assert checkio(1000) == 1
assert checkio(1111) == 1

# number = 123405
# result = 1
# # print(str(number)[2])
# for i in str(number):
#     if int(i) == 0:
#         continue
#     else:
#         result *= int(i)
# print(result)

