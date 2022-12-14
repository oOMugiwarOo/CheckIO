def checkio(line1: str, line2: str) -> str:
    c = ''
    c2 = ''
    split_line1 = line1.split(',')
    split_line2 = line2.split(',')
    for i in split_line1:
        if i in split_line2:
            c += i + ','
    for i in sorted(c.split(',')):
        if i != '':
            c2 += i + ','

    return c2[:-1]


print("Example:")
print(checkio("hello,world", "hello,earth"))

assert checkio("hello,world", "hello,earth") == "hello"
assert checkio("one,two,three", "four,five,six") == ""
assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two"
