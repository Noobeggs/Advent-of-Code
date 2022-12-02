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