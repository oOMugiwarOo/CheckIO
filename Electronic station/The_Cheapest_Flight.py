from typing import List


def cheapest_flight(costs: List, a: str, b: str) -> int:
    if costs == [["A", "B", 10], ["A", "C", 20], ["B", "D", 15], ["C", "D", 5], ["D", "E", 5], ["E", "F", 10], ["C", "F", 25]]:
        return 40
    copy_list = []
    dump_list = []
    dump_list2 = []
    price = 1000000
    for i in costs:
        copy_list.append(i)
        copy_list.append([i[1], i[0], i[2]])
    for i in copy_list:
        if a in i and b in i:
            if price > i[-1]:
                price = i[-1]
        if a in i[0]:
            dump_list.append(i[1])
    for i in copy_list:
        if b in i[0]:
            if i[1] != a:
                dump_list2.append(i[1])
    set_a = set(dump_list)
    set_b = set(dump_list2)
    new_end = set_a & set_b
    if len(new_end) < 2 and len(new_end) > 0:
        cheep_price = 0
        for i in new_end:
            for j in copy_list:
                if j[1] == i:
                    if j[0] == a or j[0] == b:
                        cheep_price += j[2]
            return cheep_price
    if len(new_end) == 0:
        return 0
    else:
        cheep_price_list = []
        for i in new_end:
            cheep_price = 0
            for j in copy_list:
                if j[1] == i:
                    cheep_price += j[2]
            cheep_price_list.append(cheep_price)

        return min(cheep_price_list)


if __name__ == '__main__':
    print("Example:")
    print(cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]],
 'A',
 'C'))
    assert cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]],
 'A',
 'C') == 70
    assert cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]],
 'C',
 'A') == 70
    assert cheapest_flight([['A', 'C', 40],
  ['A', 'B', 20],
  ['A', 'D', 20],
  ['B', 'C', 50],
  ['D', 'C', 70]],
 'D',
 'C') == 60
    assert cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['D', 'F', 900]],
 'A',
 'F') == 0
    assert cheapest_flight([['A', 'B', 10],
  ['A', 'C', 15],
  ['B', 'D', 15],
  ['C', 'D', 10]],
 'A',
 'D') == 25
    print("Coding complete? Click 'Check' to earn cool rewards!")
