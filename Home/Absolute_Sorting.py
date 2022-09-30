def checkio(values: list) -> list:
    b = [0] * len(values)
    c = []
    for i in values:
        c.append(abs(i))
    c.sort()
    for i in c:
        if i * -1 in values:
            g = c.index(i)
            b.pop(g)
            b.insert(g, i * -1)
        else:
            g = c.index(i)
            b.pop(g)
            b.insert(g, i)
    return b


print("Example:")
print(checkio([-20, -5, 10, 15]))

assert checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
assert checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
assert checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]



