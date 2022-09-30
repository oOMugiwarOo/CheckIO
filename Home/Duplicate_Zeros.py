def duplicate_zeros(donuts: list) -> list:
    b = donuts.copy()
    c = 0
    e = 0
    for i in donuts:
        if i == 0:
            d = donuts.index(i, c)
            b.insert(d + e, 0)
            e += 1
        c += 1
    return b


print("Example:")
print(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0]))

assert duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0]) == [1, 0, 0, 2, 3, 0, 0, 4, 5, 0, 0]
assert duplicate_zeros([0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0, 0]
assert duplicate_zeros([100, 10, 0, 101, 1000]) == [100, 10, 0, 0, 101, 1000]
