def is_ascending(items: list[int]) -> bool:
    if len(items) == 1 or len(items) == 0:
        return True
    elif items.count(items[0]) == len(items):
        return False
    else:
        copy_items = items.copy()
        items.sort()
        return items == copy_items


print("Example:")
print(is_ascending([-5, 10, 99, 123456]))

assert is_ascending([-5, 10, 99, 123456]) == True
assert is_ascending([99]) == True
assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
assert is_ascending([]) == True
assert is_ascending([1, 1, 1, 1]) == False
