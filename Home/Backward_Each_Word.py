def backward_string_by_word(text: str) -> str:
    if text == '':
        return ''
    else:
        exits = ''
        c = text.split(' ')
        for i in c:
            exits += i[::-1]
            exits += ' '
        return exits[:-1]


print("Example:")
print(backward_string_by_word(""))

assert backward_string_by_word("") == ""
assert backward_string_by_word("world") == "dlrow"
assert backward_string_by_word("hello world") == "olleh dlrow"
assert backward_string_by_word("hello   world") == "olleh   dlrow"
assert backward_string_by_word("welcome to a game") == "emoclew ot a emag"


# exits = ''
# b = "hello world"
# c = b.split(' ')
# print(b.split(' '))
# for i in c:
#     # if i == '' or i == ' ':
#     #     exits += ' '
#     # else:
#     exits += i[::-1]
#     exits += ' '
# print(exits[:-1])
