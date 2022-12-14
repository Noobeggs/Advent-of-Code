import aoc_lube

RAW = aoc_lube.fetch(year=2022, day=14)
print(RAW)

def parse_raw():
    paths = [[list(map(int, j.split(","))) for j in i.split(" -> ")] for i in RAW.splitlines()]
    rocks = set()
    for path in paths:
        for i in range(len(path) - 1):
            start = path[i]
            end = path[i + 1]

            if start[0] > end[0]:
                for j in range(end[0], start[0] + 1):
                    rocks.add((j, end[1]))
            elif start[0] < end[0]:
                for j in range(start[0], end[0] + 1):
                    rocks.add((j, start[1]))
            elif start[1] > end[1]:
                for j in range(end[1], start[1] + 1):
                    rocks.add((end[0], j))
            elif start[1] < end[1]:
                for j in range(start[1], end[1] + 1):
                    rocks.add((start[0], j))
    
    depth = max(map(lambda x: x[1], rocks))
    return rocks, depth

ROCKS, DEPTH = parse_raw()

def part_one():
    sand = set()
    sand_pos = source = (500, 0)
    while sand_pos[1] <= DEPTH:
        for x, y in ((0, 1), (-1, 1), (1, 1)):
            temp = sand_pos[0] + x, sand_pos[1] + y
            if temp not in ROCKS and temp not in sand:
                sand_pos = temp
                break
        else:
            sand.add(sand_pos)
            sand_pos = source
    return len(sand)

def part_two():
    sand = set()
    depth = DEPTH + 2
    sand_pos = source = (500, 0)
    while source not in sand:
        for x, y in ((0, 1), (-1, 1), (1, 1)):
            temp = sand_pos[0] + x, sand_pos[1] + y
            if temp not in ROCKS and temp not in sand and temp[1] < depth:
                sand_pos = temp
                break
        else:
            sand.add(sand_pos)
            sand_pos = source
    return len(sand)

aoc_lube.submit(year=2022, day=14, part=1, solution=part_one)
aoc_lube.submit(year=2022, day=14, part=2, solution=part_two)