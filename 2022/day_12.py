import aoc_lube
from collections import deque

RAW = aoc_lube.fetch(year=2022, day=12)
# RAW = """Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi"""
print(RAW)

def parse_raw():
    grid = [list(x) for x in RAW.splitlines()]
    for i, row in enumerate(grid):
        for j, col in enumerate(grid[i]):
            if grid[i][j] == "S":
                start = (i, j)
            if grid[i][j] == "E":
                end = (i, j)

    return grid, start, end

DATA, START, END = parse_raw()

def part_one():
    queue = deque([(START, 0)])
    visited = set([START])
    while queue:
        curr, steps = queue.popleft()
        x, y = curr
        # print("x,y", curr, "steps", steps)

        if curr == END:
            return steps

        if curr == START:
            height = ord("a")
        else:
            height = ord(DATA[curr[0]][curr[1]])
        steps += 1
        new = []
        if x > 0:
            new.append((x-1, y))
        if x < len(DATA) - 1:
            new.append((x+1, y))
        if y > 0:
            new.append((x, y-1))
        if y < len(DATA[0]) - 1:
            new.append((x, y+1))

        for point in new:
            if point == END:
                new_height = ord("z")
            else:
                new_height = ord(DATA[point[0]][point[1]])

            if point not in visited and new_height - 1 <= height:
                queue.append((point, steps))
                visited.add(point)
        

def part_two():
    queue = deque([(END, 0)])
    visited = set([END])
    while queue:
        curr, steps = queue.popleft()
        x, y = curr
        # print("x,y", curr, "steps", steps)
        if curr == START:
            height = ord("a")
        elif curr == END:
            height = ord("z")
        else:
            height = ord(DATA[curr[0]][curr[1]])

        if height == ord("a"):
            return steps

        steps += 1
        new = []
        if x > 0:
            new.append((x-1, y))
        if x < len(DATA) - 1:
            new.append((x+1, y))
        if y > 0:
            new.append((x, y-1))
        if y < len(DATA[0]) - 1:
            new.append((x, y+1))

        for point in new:
            if point == START:
                new_height = ord("a")
            elif point == END:
                new_height = ord("z")
            else:
                new_height = ord(DATA[point[0]][point[1]])
            
            if point not in visited and new_height + 1 >= height:
                queue.append((point, steps))
                visited.add(point)

aoc_lube.submit(year=2022, day=12, part=1, solution=part_one)
aoc_lube.submit(year=2022, day=12, part=2, solution=part_two)