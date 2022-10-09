ALPHABET = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 26
}

def column_number(name: str) -> int:
    list_of_letter = []
    result = 0
    if len(name) > 1:
        for i in name:
            list_of_letter.append(i)
        result = ALPHABET[list_of_letter[0]]
        for i in list_of_letter[1:]:
            result = result * 26 + ALPHABET[i]
        return result
    else:
        return ALPHABET[name]



print("Example:")
print(column_number("AA"))

assert column_number("A") == 1
assert column_number("Z") == 26
assert column_number("AB") == 28
assert column_number("ZY") == 701
assert column_number('FXSHRXW') == 2147483647

# name = 'FXSHRXW'
# list_of_letter = []
# result = 0
# if len(name) > 1:
#     for i in name:
#         list_of_letter.append(i)
#     print(list_of_letter)
#     print(ALPHABET[list_of_letter[0]])
#     print(ALPHABET[list_of_letter[0]] * 26 + ALPHABET[list_of_letter[1]])
#     print((ALPHABET[list_of_letter[0]] * 26 + ALPHABET[list_of_letter[1]]) * 26 +ALPHABET[list_of_letter[2]])
#     print(((ALPHABET[list_of_letter[0]] * 26 + ALPHABET[list_of_letter[1]]) * 26 +ALPHABET[list_of_letter[2]]) * 26 +ALPHABET[list_of_letter[3]])
#     print((((ALPHABET[list_of_letter[0]] * 26 + ALPHABET[list_of_letter[1]]) * 26 +ALPHABET[list_of_letter[2]]) * 26 +ALPHABET[list_of_letter[3]]) * 26 +ALPHABET[list_of_letter[4]])
#     print(((((ALPHABET[list_of_letter[0]] * 26 + ALPHABET[list_of_letter[1]]) * 26 +ALPHABET[list_of_letter[2]]) * 26 +ALPHABET[list_of_letter[3]]) * 26 +ALPHABET[list_of_letter[4]]) * 26 +ALPHABET[list_of_letter[5]])
#     print((((((ALPHABET[list_of_letter[0]] * 26 + ALPHABET[list_of_letter[1]]) * 26 +ALPHABET[list_of_letter[2]]) * 26 +ALPHABET[list_of_letter[3]]) * 26 +ALPHABET[list_of_letter[4]]) * 26 +ALPHABET[list_of_letter[5]]) * 26 +ALPHABET[list_of_letter[6]])
#     result = ALPHABET[list_of_letter[0]]
#     for i in list_of_letter[1:]:
#         result *= 26
#         result += ALPHABET[i]
#         print(result)
# else:
#     print(ALPHABET[name])

