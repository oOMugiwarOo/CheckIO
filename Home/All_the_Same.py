from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:

    if len(elements) == 0:
        return True

    elif elements.count(elements[0]) == len(elements):
        return True

    else:
        return False


print("Example:")
print(all_the_same([1, 1, 1]))

assert all_the_same([1, 1, 1]) == True
assert all_the_same([1, 2, 1]) == False
assert all_the_same([1, 1, 1, 2]) == False
assert all_the_same([2, 1, 1, 1]) == False
assert all_the_same([]) == True
assert all_the_same([1]) == True

# a = []
#
# if len(a) == 0:
#     print(2)
#
# elif a.count(a[0]) == len(a):
#     print(1)
#
# else:
#     print(3)
