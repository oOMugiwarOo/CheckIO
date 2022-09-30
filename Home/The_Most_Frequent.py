def most_frequent(data: list[str]) -> str:
    counter = 0
    index = 0
    for i in data:
        if data.count(i) > counter:
            index = data.index(i)
            counter += data.count(i)
    return data[index]


print("Example:")
print(most_frequent(["a", "b", "c", "a", "b", "a"]))

assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"
assert most_frequent(['a', 'a', 'z']) == 'a'

# a = ['a', 'a', 'z']
# counter = 0
# index = 0
# for i in a:
#     if a.count(i) >= counter:
#         print(a.count(i))
#         index = a.index(i)
#         counter += a.count(i)
# print(a[index])
