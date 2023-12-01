import aoc_lube

RAW = aoc_lube.fetch(year=2023, day=1)
print(RAW)

def parse_raw():
    return RAW.splitlines()

DATA = parse_raw()

def part_one():
    sum = 0
    for line in DATA:
        for c in line:
            if c.isdigit():
                sum += int(c) * 10
                break
        for c in line[::-1]:
            if c.isdigit():
                sum += int(c)
                break
    return sum

LUT = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

# DATA = """two1nine,
# eightwothree,
# abcone2threexyz,
# xtwone3four,
# 4nineeightseven2,
# zoneight234,
# 7pqrstsixteen""".split(",")

def part_two():
    sum = 0
    for line in DATA:
        print(line)
        first = -1
        first_i = -1
        last = -1
        last_i = -1
        for i, c in enumerate(line):
            if c.isdigit():
                first = int(c)
                first_i = i
                break
        for i, c in enumerate(line[::-1]):
            if c.isdigit():
                last = int(c)
                last_i = len(line) - i - 1
                break
        print(first_i, first, last_i, last)
        for key in LUT:
            index = line.find(key)
            if index != -1:
                temp = first_i
                if temp == -1:
                    first_i = index
                first_i = min(first_i, index)
                if temp != first_i:
                    first = LUT[key]
                    print(f"first: {first_i} {first}")
            index = line.rfind(key)
            if index != -1:
                temp = last_i
                last_i = max(last_i, index)
                if temp != last_i:
                    last = LUT[key]
                    print(f"last: {last_i} {last}")
        print(f"ans:{first}{last}")
        sum += first * 10
        sum += last
    return sum

aoc_lube.submit(year=2023, day=1, part=1, solution=part_one)
aoc_lube.submit(year=2023, day=1, part=2, solution=part_two)
