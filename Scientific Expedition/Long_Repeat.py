def long_repeat(line: str) -> int:
    letter = line[0]
    counter = 0
    list_of_counter = []
    for i in line:
        if i == letter:
            counter += 1
        else:
            list_of_counter.append(counter)
            letter = i
            counter = 1
    list_of_counter.append(counter)
    return max(list_of_counter)


print("Example:")
print(long_repeat("sdsffffse"))

assert long_repeat("sdsffffse") == 4
assert long_repeat("ddvvrwwwrggg") == 3
