# def cheapest_flight(data, start, stop):
#     stack, found, best = [(start, 0)], False, 1e9
#     while stack:
#         path, price = stack.pop()
#         if path[-1] == stop:
#             best, found = min(best, price), True
#             continue
#         for a, b, p in data:
#             stack += [(path+b, price+p)]*(a == path[-1] and b not in path)
#             stack += [(path+a, price+p)]*(b == path[-1] and a not in path)
#     return best*found
#
# if __name__ == '__main__':
#     print("Example:")
#     print(cheapest_flight([['A', 'C', 100],
#   ['A', 'B', 20],
#   ['B', 'C', 50]],
#  'A',
#  'C'))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert cheapest_flight([['A', 'C', 100],
#   ['A', 'B', 20],
#   ['B', 'C', 50]],
#  'A',
#  'C') == 70
#     assert cheapest_flight([['A', 'C', 100],
#   ['A', 'B', 20],
#   ['B', 'C', 50]],
#  'C',
#  'A') == 70
#     assert cheapest_flight([['A', 'C', 40],
#   ['A', 'B', 20],
#   ['A', 'D', 20],
#   ['B', 'C', 50],
#   ['D', 'C', 70]],
#  'D',
#  'C') == 60
#     assert cheapest_flight([['A', 'C', 100],
#   ['A', 'B', 20],
#   ['D', 'F', 900]],
#  'A',
#  'F') == 0
#     assert cheapest_flight([['A', 'B', 10],
#   ['A', 'C', 15],
#   ['B', 'D', 15],
#   ['C', 'D', 10]],
#  'A',
#  'D') == 25
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# data = [["A","B",10],["A","C",20],["B","D",15],["C","D",5],["D","E",5],["E","F",10],["C","F",25]]
# start = 'A'
# stop = 'F'
# stack, found, best = [(start, 0)], False, 1e9
# # print(stack)
# # print(found)
# # print(best)
# while stack:
#     path, price = stack.pop()
#     print(fr'path = {path}')
#     print(fr'price = {price}')
#     if path[-1] == stop:
#         best, found = min(best, price), True
#         continue
#     for a, b, p in data:
#         print(fr'a b p = {a,b,p}')
#         stack += [(path+b, price+p)]*(a == path[-1] and b not in path)
#         stack += [(path+a, price+p)]*(b == path[-1] and a not in path)
#     print(fr'stack = {stack}')
# print(best*found)


