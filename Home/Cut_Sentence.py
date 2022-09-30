def cut_sentence(line: str, length: int) -> str:
    """
    Cut a given sentence, so it becomes shorter than or equal to a given length.
    """
    if len(line) <= length:
        return line
    else:
        answer = ''
        d = 0
        c = line.split()
        for i in c:
            if d + len(i) <= length:
                answer += i + ' '
                d += len(i) + 1
            else:
                break
        return answer[:-1] + '...'


print("Example:")
print(cut_sentence("Hi my name is Alex", 4))

assert cut_sentence("Hi my name is Alex", 10) == "Hi my name..."
assert cut_sentence("Hi my name is Alex", 4) == "Hi..."
assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex"
assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex"







