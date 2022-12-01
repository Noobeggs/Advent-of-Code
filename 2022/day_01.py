import aoc_lube

RAW = aoc_lube.fetch(year=2022, day=1)
print(RAW)

def parse_raw():
    return list(RAW.split("\n\n"))

DATA = parse_raw()
# print(DATA)

a = sorted(map(lambda x: sum(map(int, x.split("\n"))), DATA))

def part_one():
    return a[-1]

def part_two():
    return sum(a[-3:])

aoc_lube.submit(year=2022, day=1, part=1, solution=part_one)
aoc_lube.submit(year=2022, day=1, part=2, solution=part_two)