def remove_min_max(data: set[int], total: int) -> set[int]:

    for i in range(total):
        if data != set():
            data.remove(max(data))
            if data != set():
                data.remove(min(data))

    return data


# print("Example:")
# print(remove_min_max({4, 5, 6, 7}, 1))

assert remove_min_max({8, 9, 18, 7}, 1) == {8, 9}
assert remove_min_max({8, 9, 7}, 0) == {8, 9, 7}
assert remove_min_max({8, 9, 7}, 2) == set()
assert remove_min_max({1, 2, 7, 8, 9}, 2) == {7}
assert remove_min_max(set(), 1) == set()


# a = {8, 9, 7}
# c = 2
#
# for i in range(c):
#     if a != set():
#         a.remove(max(a))
#         if a != set():
#             a.remove(min(a))
#
# print(a)

