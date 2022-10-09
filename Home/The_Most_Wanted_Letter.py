import string


def checkio(text: str) -> str:
    alphabet = string.ascii_lowercase
    b = ''
    c = 0
    for i in text.lower():
        if text.lower().count(i) > c and i.isalpha():
            c = text.lower().count(i)
            b = i
        elif text.lower().count(i) == c:
            try:
                if alphabet.index(i) < alphabet.index(b) and i.isalpha():
                    b = i
                else:
                    continue
            except ValueError:
                continue
    return b


print("Example:")
print(checkio("Hello World!"))

assert checkio("Hello World!") == "l"
assert checkio("How do you do?") == "o"
assert checkio("One") == "e"
assert checkio("Oops!") == "o"
assert checkio("AAaooo!!!!") == "a"
assert checkio("abe") == "a"
