def bigger_price(limit: int, data: list[dict]) -> list[dict]:
    """
    TOP most expensive goods
    """
    dump_list = []
    while data != []:
        counter = 0
        for i in data:
            if i['price'] > counter:
                counter = i['price']
        for i in data:
            if i['price'] == counter:
                dump_list.append(i)
                data.remove(i)
    return dump_list[:limit]


print("Example:")
print(
    bigger_price(
        2,
        [
            {"name": "bread", "price": 100},
            {"name": "wine", "price": 138},
            {"name": "meat", "price": 15},
            {"name": "water", "price": 1},
        ],
    )
)

assert bigger_price(
    2,
    [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1},
    ],
) == [{"name": "wine", "price": 138}, {"name": "bread", "price": 100}]
assert bigger_price(
    1, [{"name": "pen", "price": 5}, {"name": "whiteboard", "price": 170}]
) == [{"name": "whiteboard", "price": 170}]

# a = [
#             {"name": "bread", "price": 100},
#             {"name": "wine", "price": 138},
#             {"name": "meat", "price": 15},
#             {"name": "water", "price": 1},
#         ]
# dump_list = []
# while a != []:
#     counter = 0
#     for i in a:
#         if i['price'] > counter:
#             counter = i['price']
#     for i in a:
#         if i['price'] == counter:
#             dump_list.append(i)
#             a.remove(i)
# print(dump_list)
