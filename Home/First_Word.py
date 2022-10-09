def first_word(text: str) -> str:
    """
    function returns the first word in a given text.
    """
    if ',' in text:
        words = text.split(',')
        for i in words:
            if i.isalpha():
                return i
    elif '\'' in text:
        words = text.split(' ')
        for i in words:
            if '\'' in i:
                return i
    elif ' ' in text:
        words = text.split(' ')
        for i in words:
            if i.isalpha():
                return i
    elif text.isalpha():
        return text
    else:
        words = text.split('.')
        for i in words:
            if i.isalpha():
                return i


print("Example:")
print(first_word("Hello world"))

assert first_word("Hello world") == "Hello"
assert first_word(" a word ") == "a"
assert first_word("don't touch it") == "don't"
assert first_word("greetings, friends") == "greetings"
assert first_word("... and so on ...") == "and"
assert first_word("hi") == "hi"
assert first_word('Hello.World') == "Hello"
