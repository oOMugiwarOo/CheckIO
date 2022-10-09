def sum_by_types(items: list[str, int]) -> tuple[str, int] | list[str, int]:
    a = 0
    c = ''
    for i in range(len(items)):
        if type(items[i]) == str:
            c += items[i]
        elif type(items[i]) == int:
            a += items[i]
    return [c, a]


print("Example:")
print(list(sum_by_types([])))

assert list(sum_by_types([])) == ["", 0]
assert list(sum_by_types([1, 2, 3])) == ["", 6]
assert list(sum_by_types(["1", 2, 3])) == ["1", 5]
assert list(sum_by_types(["1", "2", 3])) == ["12", 3]
assert list(sum_by_types(["1", "2", "3"])) == ["123", 0]
assert list(sum_by_types(["size", 12, "in", 45, 0])) == ["sizein", 57]
