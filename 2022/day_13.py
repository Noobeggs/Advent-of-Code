import aoc_lube
from functools import cmp_to_key

RAW = aoc_lube.fetch(year=2022, day=13)
# RAW = """[1,1,3,1,1]
# [1,1,5,1,1]

# [[1],[2,3,4]]
# [[1],4]

# [9]
# [[8,7,6]]

# [[4,4],4,4]
# [[4,4],4,4,4]

# [7,7,7,7]
# [7,7,7]

# []
# [3]

# [[[]]]
# [[]]

# [1,[2,[3,[4,[5,6,7]]]],8,9]
# [1,[2,[3,[4,[5,6,0]]]],8,9]"""
print(RAW)

def parse_raw():
    return [(eval(packet) for packet in pairs.splitlines()) for pairs in RAW.split("\n\n")]

def parse_raw_two():
    return [eval(packet) for packet in RAW.splitlines() if packet != ""]

DATA = parse_raw()
DATA_TWO = parse_raw_two()
print(DATA)

def compare_lists(l1, l2, level=0):
    # print("recursion level", level)
    ans = 0
    n = min(len(l1), len(l2))
    for i in range(n):
        if type(l1[i]) == type(l2[i]) == int:
            if l1[i] < l2[i]:
                return 1
            elif l1[i] > l2[i]:
                return -1
            else:
                continue
        elif type(l1[i]) == type(l2[i]) == list:
            ans = compare_lists(l1[i], l2[i], level=level+1)
        else:
            if type(l1[i]) == int:
                ans = compare_lists([l1[i]], l2[i], level=level+1)
            elif type(l2[i]) == int:
                ans = compare_lists(l1[i], [l2[i]], level=level+1)
        if ans != 0:
            return ans
    if len(l1) < len(l2):
        return 1
    elif len(l1) > len(l2):
        return -1
    else:
        return 0

def part_one():
    ans = 0
    for index, (p1, p2) in enumerate(DATA, 1):
        print(p1, p2)
        order = compare_lists(p1, p2)
        if order == 1:
            ans += index

    return ans

def part_two():
    DATA_TWO.append([[2]])
    DATA_TWO.append([[6]])
    DATA_TWO.sort(key=cmp_to_key(compare_lists), reverse=True)
    # print(DATA_TWO)
    ans = (DATA_TWO.index([[2]]) + 1) * (DATA_TWO.index([[6]]) + 1)
    return ans

aoc_lube.submit(year=2022, day=13, part=1, solution=part_one)
aoc_lube.submit(year=2022, day=13, part=2, solution=part_two)