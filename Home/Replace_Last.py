from typing import Iterable


def replace_last(line: list) -> Iterable:
    if len(line) == 0:
        return []
    else:
        line2 = line[:-1]
        line2.insert(0, line[-1])
        return line2


print("Example:")
print(list(replace_last([2, 3, 4, 1])))

assert list(replace_last([2, 3, 4, 1])) == [1, 2, 3, 4]
assert list(replace_last([1, 2, 3, 4])) == [4, 1, 2, 3]
assert list(replace_last([1])) == [1]
assert list(replace_last([])) == []

# a = [2, 3, 4, 1]
# print(a[:-1])
# b = a[:-1]
# b.insert(0, a[-1])
# print(b)
#
# print(a[-1])
