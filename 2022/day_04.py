import aoc_lube

RAW = aoc_lube.fetch(year=2022, day=4)
print(RAW)

def parse_raw():
    return RAW.splitlines()

DATA = parse_raw()

def part_one():
    count = 0
    for pair in DATA:
        start_pair = [0, 0]
        end_pair = [0, 0]
        elves = pair.split(',')
        for i, elf in enumerate(elves):
            range = tuple(map(int, elf.split('-')))
            start_pair[i] = range[0]
            end_pair[i] = range[1]
        if start_pair[0] <= start_pair[1] and end_pair[0] >= end_pair[1]:
            count += 1
        elif start_pair[1] <= start_pair[0] and end_pair[1] >= end_pair[0]:
            count += 1
    return count

def part_two():
    count = 0
    for pair in DATA:
        start_pair = [0, 0]
        end_pair = [0, 0]
        elves = pair.split(',')
        for i, elf in enumerate(elves):
            range = tuple(map(int, elf.split('-')))
            start_pair[i] = range[0]
            end_pair[i] = range[1]
        if start_pair[0] <= start_pair[1] <= end_pair[0] or start_pair[0] <= end_pair[1] <= end_pair[0]:
            count += 1
        elif start_pair[1] <= start_pair[0] <= end_pair[1] or start_pair[1] <= end_pair[0] <= end_pair[1]:
            count += 1
    return count


aoc_lube.submit(year=2022, day=4, part=1, solution=part_one)
aoc_lube.submit(year=2022, day=4, part=2, solution=part_two)