def count_gold(pyramid):
    """
    Return max possible sum in a path from top to bottom
    """
    work = list(list(row) for row in pyramid)
    for i in range(len(work) - 1, 0, -1):
        if i == len(work) - 1:
            pass
        else:
            for j in range(len(work[i])):
                work[i][j] += max(work[i + 1][j], work[i + 1][j + 1])
    return work[0][0] + (max(work[1][0], work[1][1]))



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23, "First example"
    assert count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15, "Second example"
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"

# pyramid = (
#         (1,),
#         (2, 1),
#         (1, 2, 1),
#         (1, 2, 1, 1),
#         (1, 2, 1, 1, 1),
#         (1, 2, 1, 1, 1, 1),
#         (1, 2, 1, 1, 1, 1, 9)
#     )
# counter = 0
# # print(len(a))
# for i in a[::-1]:
#     # print(a.index(i))
#     print(i)
# print(fr'summ = {counter}')


# work = list(list(row) for row in pyramid)
# print(work)
# for i in range(len(work) - 1, 0 , -1):
#     print(fr'i = {i}')
#     if i == len(work) - 1:
#         pass
#     else:
#         for j in range(len(work[i])):
#             print(fr'j = {j}')
#             print(fr'work[{i}][{j}] = {work[i][j]}')
#             work[i][j] += max(work[i + 1][j], work[i + 1][j + 1])
#             print(fr'work[{i}][{j}] = {work[i][j]}')
# print(work[0][0] + (max(work[1][0], work[1][1])))
# a = 1
# for i in range(a):
#     print(i)
#     a += 1
#     if a > 100:
#         break

