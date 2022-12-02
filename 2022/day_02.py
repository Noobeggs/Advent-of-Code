import aoc_lube

RAW = aoc_lube.fetch(year=2022, day=2)
print(RAW)

def parse_raw():
    return map(str.split, RAW.splitlines())

DATA = parse_raw()

def part_one():
    score = 0
    for opp_move, my_move in DATA:
        score += " XYZ".index(my_move)
        score += 3 * ("ABC".index(opp_move) == "XYZ".index(my_move))
        score += 6 * ("CAB".index(opp_move) == "XYZ".index(my_move))
    return score

def part_two():
    score = 0
    for opp_move, result in DATA:
        score += 3 * "XYZ".index(result)
        if result == "X":
            score += " BCA".index(opp_move)
        elif result == "Y":
            score += " ABC".index(opp_move)
        elif result == "Z":
            score += " CAB".index(opp_move)
    return score

aoc_lube.submit(year=2022, day=2, part=1, solution=part_one)
aoc_lube.submit(year=2022, day=2, part=2, solution=part_two)

"""
Some other alternative solutions I found interesting
"""
# Modified from Sevoi#5028 from Python Discord
def parse_raw():
    return [(" ABC".index(line[0]), " XYZ".index(line[2])) for line in RAW.splitlines()]

DATA = parse_raw()
print(DATA)

def part_one():
    score = 0
    for round in DATA:
        score += round[1]
        if round[0] == round[1]:
            score += 3
        elif (round[0]) % 3 == (round[1] - 1):
            score += 6
    return score

print(part_one())

def part_two():
    score = 0
    for round in DATA:
        score += 3 * (round[1] - 1)
        score += (round[0] + round[1]) % 3 + 1
    return score

print(part_two())