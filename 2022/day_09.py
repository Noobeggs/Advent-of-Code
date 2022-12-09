import aoc_lube

RAW = aoc_lube.fetch(year=2022, day=9)
# RAW = """R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2"""
print(RAW)

def parse_raw():
    return RAW.splitlines()

DATA = parse_raw()

class Point():
    def __init__(self):
        self.x = 0
        self.y = 0

    def pos(self):
        return (self.x, self.y)

def part_one():
    visited = set()
    head = Point()
    tail = Point()
    visited.add((0, 0))

    for line in DATA:
        direction, length = line.split()
        for _ in range(int(length)):
            if direction == "U":
                head.y += 1
            elif direction == "D":
                head.y -= 1
            elif direction == "L":
                head.x -= 1
            elif direction == "R":
                head.x += 1
            if head.x != tail.x and head.y != tail.y and (abs(head.x - tail.x) > 1 or abs(head.y - tail.y) > 1):
                if head.x > tail.x:
                    tail.x += 1
                else:
                    tail.x -= 1
                if head.y > tail.y:
                    tail.y += 1
                else:
                    tail.y -= 1
            elif abs(head.x - tail.x) > 1:
                if head.x > tail.x:
                    tail.x += 1
                else:
                    tail.x -= 1
            elif abs(head.y - tail.y) > 1:
                if head.y > tail.y:
                    tail.y += 1
                else:
                    tail.y -= 1
            visited.add(tail.pos())

    return len(visited)

def part_two():
    visited = set()
    knots = [Point() for _ in range(10)]
    visited.add((0, 0))
    
    for line in DATA:
        direction, length = line.split()
        for _ in range(int(length)):
            if direction == "U":
                knots[0].y += 1
            elif direction == "D":
                knots[0].y -= 1
            elif direction == "L":
                knots[0].x -= 1
            elif direction == "R":
                knots[0].x += 1

            for i, knot in enumerate(knots[1:]):
                if knots[i].x != knot.x and knots[i].y != knot.y and (abs(knots[i].x - knot.x) > 1 or abs(knots[i].y - knot.y) > 1):
                    if knots[i].x > knot.x:
                        knot.x += 1
                    else:
                        knot.x -= 1
                    if knots[i].y > knot.y:
                        knot.y += 1
                    else:
                        knot.y -= 1
                elif abs(knots[i].x - knot.x) > 1:
                    if knots[i].x > knot.x:
                        knot.x += 1
                    else:
                        knot.x -= 1
                elif abs(knots[i].y - knot.y) > 1:
                    if knots[i].y > knot.y:
                        knot.y += 1
                    else:
                        knot.y -= 1
            visited.add(knots[9].pos())
    
    return len(visited)

aoc_lube.submit(year=2022, day=9, part=1, solution=part_one)
aoc_lube.submit(year=2022, day=9, part=2, solution=part_two)