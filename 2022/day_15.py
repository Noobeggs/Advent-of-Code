import aoc_lube
import re

RAW = aoc_lube.fetch(year=2022, day=15)
# RAW = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
# Sensor at x=13, y=2: closest beacon is at x=15, y=3
# Sensor at x=12, y=14: closest beacon is at x=10, y=16
# Sensor at x=10, y=20: closest beacon is at x=10, y=16
# Sensor at x=14, y=17: closest beacon is at x=10, y=16
# Sensor at x=8, y=7: closest beacon is at x=2, y=10
# Sensor at x=2, y=0: closest beacon is at x=2, y=10
# Sensor at x=0, y=11: closest beacon is at x=2, y=10
# Sensor at x=20, y=14: closest beacon is at x=25, y=17
# Sensor at x=17, y=20: closest beacon is at x=21, y=22
# Sensor at x=16, y=7: closest beacon is at x=15, y=3
# Sensor at x=14, y=3: closest beacon is at x=15, y=3
# Sensor at x=20, y=1: closest beacon is at x=15, y=3"""
print(RAW)

def parse_raw():
    return [list(map(int, re.findall(r'-?\d+', line))) for line in RAW.splitlines()]

DATA = parse_raw()
print(DATA)

def part_one():
    beaconless = set()
    beacons = set()
    target_row = 2_000_000
    # target_row = 10
    for sx, sy, bx, by in DATA:
        if by == target_row:
            beacons.add(bx)
        distance = abs(sx - bx) + abs(sy - by)
        target_range = distance - abs(sy - target_row)
        for n in range(sx - target_range, sx + target_range + 1):
            beaconless.add(n)

    ans = len(beaconless)
    for beacon in beacons:
        if beacon in beaconless:
            ans -= 1
    return ans

def part_two():
    search_range = 4_000_000
    # search_range = 20

    for row_no in range(search_range + 1):
        ranges = []
        for sx, sy, bx, by in DATA:
            distance = abs(sx - bx) + abs(sy - by)
            row_range = distance - abs(sy - row_no)
            ranges.append((sx - row_range, sx + row_range))
        ranges.sort()

        range_end = ranges[0][1]

        for i in range(len(ranges) - 1):
            a, b = ranges[i], ranges[i + 1]
            range_end = max(range_end, a[1])

            if b[0] > range_end + 1 and 0 <= range_end + 1 <= search_range:
                print(ranges)
                print(i, range_end + 1, row_no)
                return (range_end + 1) * 4_000_000 + row_no

aoc_lube.submit(year=2022, day=15, part=1, solution=part_one)
aoc_lube.submit(year=2022, day=15, part=2, solution=part_two)