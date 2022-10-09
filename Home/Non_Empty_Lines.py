def non_empty_lines(text: str) -> int:
    counter = 0
    for i in text.split('\n'):
        if i == '':
            pass
        elif i[0].isalpha():
            counter += 1

    return counter


print("Example:")
print(non_empty_lines("one simple line\n"))

assert non_empty_lines("one simple line\n") == 1
assert non_empty_lines("") == 0
assert non_empty_lines("\nonly one line\n            ") == 1
assert (
    non_empty_lines(
        "\nLorem ipsum dolor sit amet,\n\nconsectetur adipiscing elit\nNam odio nisi, aliquam\n            "
    )
    == 3
)

a = '\nLorem ipsum dolor sit amet,\n\nconsectetur adipiscing elit\nNam odio nisi, aliquam\nNullam ante ligula,\n' \
    ' \n fermentum a porta\n '
