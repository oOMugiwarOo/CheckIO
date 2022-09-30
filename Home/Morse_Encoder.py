MORSE = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}


def morse_encoder(text: str) -> str:
    b = ''
    for i in text.lower():
        if i != ' ':
            b += MORSE[i] + ' '
        elif i == ' ':
            b += '  '
    return b[:-1]


print("Example:")
print(morse_encoder("some text"))

assert morse_encoder("some text") == "... --- -- .   - . -..- -"
assert (
    morse_encoder("I was born in 1990")
    == "..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----"
)

# a = 'some text'
# b = ''
# c = ''
# for i in a:
#     if i != ' ':
#         b += MORSE[i] + ' '
#     elif i == ' ':
#         b += ' '
# print(b)
# for i in b.split(' '):
#     if i == '':
#         c += ' '
#     else:
#         c += i
# print(c.capitalize())
