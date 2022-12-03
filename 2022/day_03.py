import aoc_lube

RAW = aoc_lube.fetch(year=2022, day=3)
print(RAW)

def parse_raw():
    return [(rs[:len(rs)//2], rs[len(rs)//2:]) for rs in RAW.splitlines()]

DATA = parse_raw()

def part_one():
    prio_sum = 0
    for rs in DATA:
        for i in rs[0]:
            if i in rs[1]:
                if i.islower():
                    prio_sum += ord(i) - ord('a') + 1
                else:
                    prio_sum += ord(i) - ord('A') + 27
                break
                # prio_sum += ord(i) - ((ord('a') - 1) if i.islower() else (ord('A') - 27))
    return prio_sum

def parse_raw_two():
    rs = RAW.splitlines()
    return [rs[i:i + 3] for i in range(0, len(rs), 3)]

DATA_TWO = parse_raw_two()

def part_two():
    prio_sum = 0
    for group in DATA_TWO:
        for i in group[0]:
            if i in group[1] and i in group[2]:
                if i.islower():
                    prio_sum += ord(i) - ord('a') + 1
                else:
                    prio_sum += ord(i) - ord('A') + 27
                break
    return prio_sum

aoc_lube.submit(year=2022, day=3, part=1, solution=part_one)
aoc_lube.submit(year=2022, day=3, part=2, solution=part_two)