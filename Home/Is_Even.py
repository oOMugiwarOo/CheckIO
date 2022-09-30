def is_even(num: int) -> bool:
    if num % 2 == 1:
        return False
    else:
        return True

print('Example:')
print(is_even(2))

assert is_even(2) == True
assert is_even(5) == False
assert is_even(0) == True

