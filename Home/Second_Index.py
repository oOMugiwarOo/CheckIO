def second_index(text: str, symbol: str) -> [int, None]:
    """
    returns the second index of a symbol in a given text
    """
    if symbol in text:
        try:
            return text.index(symbol) + text[text.index(symbol) + 1:].index(symbol) + 1
        except ValueError:
            return None
    else:
        return None



print("Example:")
print(second_index("sims", "s"))

assert second_index("sims", "s") == 3
assert second_index("find the river", "e") == 12
assert second_index("hi", " ") == None
assert second_index("hi mayor", " ") == None
assert second_index("hi mr Mayor", " ") == 5

# a = "hi mayor"
# find = ' '
# print(a.index(find))
# print(a[a.index(find)+1:].index(find))
# print(a.index(find) + a[a.index(find)+1:].index(find) +1)
