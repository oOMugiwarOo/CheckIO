FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    if number % 100 == 0:
        return FIRST_TEN[(number // 100) - 1] + ' ' + HUNDRED
    if number % 100 < 20:
        if number < 10:
            return FIRST_TEN[number - 1]
        if 9 < number < 20:
            return SECOND_TEN[number - 10]
        if number > 99:
            if number % 100 < 10:
                return FIRST_TEN[(number // 100) - 1] + ' ' + HUNDRED + ' ' + FIRST_TEN[(number % 100) - 1]
            if 9 < number % 100 < 20:
                return FIRST_TEN[(number // 100) - 1] + ' ' + HUNDRED + ' ' + SECOND_TEN[(number % 100) - 10]
    if 19 < number < 100:
        if number % 10 == 0:
            return OTHER_TENS[(number // 10) - 2]
        else:
            return OTHER_TENS[(number // 10) - 2] + ' ' + FIRST_TEN[(number % 10) - 1]
    else:
        if (number % 100) % 10 == 0:
            return FIRST_TEN[(number // 100) - 1] + ' ' + HUNDRED + ' ' + OTHER_TENS[((number % 100) // 10) - 2]
        else:
            return FIRST_TEN[(number // 100) - 1] + ' ' + HUNDRED + ' ' + OTHER_TENS[((number % 100) // 10) - 2] + ' ' + FIRST_TEN[(number % 10) - 1]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"


# a = 400
# if a % 100 == 0:
#     print(FIRST_TEN[(a//100)-1] + ' ' + HUNDRED)
# if a % 100 < 20:
#     if a < 10:
#         print(FIRST_TEN[a-1])
#     if 9 < a < 20:
#         print(SECOND_TEN[a-10])
#     if a > 99:
#         if a % 100 < 10:
#             print(FIRST_TEN[(a//100)-1] + ' ' + HUNDRED + ' ' + FIRST_TEN[(a % 100) - 1])
#         if 9 < a % 100 < 20:
#             print(FIRST_TEN[(a//100)-1] + ' ' + HUNDRED + ' ' + SECOND_TEN[(a % 100) - 10])
# if 19 < a < 100:
#     if a % 10 == 0:
#         print(OTHER_TENS[(a // 10) - 2])
#     else:
#         print(OTHER_TENS[(a // 10) - 2] + ' ' + FIRST_TEN[(a % 10) - 1])
# else:
#     if (a % 100) % 10 == 0:
#         print(FIRST_TEN[(a // 100) - 1] + ' ' + HUNDRED + ' ' + OTHER_TENS[((a % 100) // 10) - 2])
#     else:
#         print(FIRST_TEN[(a//100)-1] + ' ' + HUNDRED + ' ' + OTHER_TENS[((a % 100) // 10) - 2] + ' ' + FIRST_TEN[(a % 10) - 1])

