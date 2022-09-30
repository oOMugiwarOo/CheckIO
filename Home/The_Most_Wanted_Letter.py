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

alphabet = string.ascii_lowercase
a = 'a-z'
b = ''
c = 0
for i in a.lower():
    if a.lower().count(i) > c and i.isalpha():
        c = a.lower().count(i)
        b = i
    elif a.lower().count(i) == c:
        try:
            if alphabet.index(i) < alphabet.index(b) and i.isalpha():
                b = i
            else:
                continue
        except ValueError:
            continue


print(b)
print(c)
# print(a.lower().count('a'))
# print(alphabet.index('e') < alphabet.index('o'))



