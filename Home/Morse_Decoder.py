MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}


def morse_decoder(code: str) -> str:
    b = ''
    c = ''
    for i in code.split(' '):
        if i != '':
            b += MORSE[i]
        elif i == '':
            b += ' '

    for i in b.split(' '):
        if i == '':
            c += ' '
        else:
            c += i

    return c.capitalize()


print("Example:")
print(morse_decoder("... --- -- .   - . -..- -"))

assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
assert (
    morse_decoder("..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----")
    == "I was born in 1990"
)

# a = '..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----'
# b = ''
# c = ''
# for i in a.split(' '):
#     if i != '':
#         b += MORSE[i]
#     elif i == '':
#         b += ' '
# print(b)
# for i in b.split(' '):
#     if i == '':
#         c += ' '
#     else:
#         c += i
# print(c.capitalize())


# print(MORSE.values())
# print(MORSE.keys())
# print(MORSE['...'])
