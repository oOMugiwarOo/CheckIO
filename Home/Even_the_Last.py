def checkio(array: list[int]) -> int:
    if len(array) == 0:
        return 0
    else:
        counter = 0
        summ = 0
        for i in array:
            if counter % 2 == 0:
                summ += i
            counter += 1
        return summ * array[-1]


print("Example:")
print(checkio([0, 1, 2, 3, 4, 5]))

assert checkio([0, 1, 2, 3, 4, 5]) == 30
assert checkio([1, 3, 5]) == 30
assert checkio([6]) == 36
assert checkio([]) == 0
