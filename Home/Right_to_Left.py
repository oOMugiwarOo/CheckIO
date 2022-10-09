def left_join(phrases: tuple) -> str:
    """
    Join strings and replace "right" to "left"
    """
    counter = ''
    for i in phrases:
        for j in i:
            counter += j
            if 'right' in counter:
                counter = counter[:-5] + 'left'
        counter += ','
    return counter[:-1]


print("Example:")
print(left_join(("left", "right", "left", "stop")))

assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
assert left_join(("bright aright", "ok")) == "bleft aleft,ok"
assert left_join(("brightness wright",)) == "bleftness wleft"
assert left_join(("enough", "jokes")) == "enough,jokes"
