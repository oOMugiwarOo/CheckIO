def best_stock(data: dict[str, float]) -> str:
    counter = 0
    for key in data.keys():
        if counter < data[key]:
            counter = data[key]

    for value in data.items():
        if value[1] == counter:
            stock = value[0]
    return stock


print("Example:")
print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))

assert best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
assert best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"

a = {"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}

# print(a.keys())
# print(a.values())
# b = a.values()
# print(b)
# counter = 0
# for key in a.keys():
#     if counter < a[key]:
#         counter = a[key]
# print(counter)
# for value in a.items():
#     if value[1] == counter:
#         print(value[0])


