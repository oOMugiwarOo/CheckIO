def checkio(number):
    minutes = 1
    birds = []
    while number > 0:
        birds += [0] * minutes
        for i in range(len(birds)):
            birds[i] += 1
            number -= 1
            if number == 0:
                break
        minutes += 1
    return len(birds)-birds.count(0)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(3) == 2, "3rd example"
    assert checkio(10) == 6, "4th example"


# korm = 53
# minutes = 1
# birds = []
# while korm > 0:
#     birds += [0] * minutes
#     print(minutes)
#     for i in range(len(birds)):
#         birds[i] += 1
#         print(birds)
#         korm -= 1
#         if korm == 0:
#             break
#     minutes += 1
# print(len(birds)-birds.count(0))

