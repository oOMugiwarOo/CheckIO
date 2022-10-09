def goes_after(word: str, first: str, second: str) -> bool:
    d = first + second
    if first in word and second in word:
        if word.count(first) == 1 and word.count(second) == 1:
            if d in word:
                return True
            else:
                return False
        else:
            first1 = word.rindex(first)
            second2 = word.rindex(second)
            if first1 > second2:
                string = word[:first1]
                if d in string:
                    return True
            else:
                string = word[:second2]
                if d in string:
                    return True
            return False
    else:
        return False


print("Example:")
print(goes_after("world", "w", "o"))

assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("panorama", "a", "n") == True
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False
assert goes_after('almaz', 'm', 'a') == False
