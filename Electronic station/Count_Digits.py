def count_digits(text: str) -> int:
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = 0
    for i in array:
        result += text.count(str(i))
    return result


print("Example:")
print(count_digits("hi"))

assert count_digits("hi") == 0
assert count_digits("who is 1st here") == 1
assert count_digits("my numbers is 2") == 1
assert (
    count_digits(
        "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
    )
    == 8
)
assert count_digits("5 plus 6 is") == 2
assert count_digits("") == 0
