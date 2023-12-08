import aoc_lube

RAW = aoc_lube.fetch(year=2023, day=8)
### 2 steps
# RAW = """RL

# AAA = (BBB, CCC)
# BBB = (DDD, EEE)
# CCC = (ZZZ, GGG)
# DDD = (DDD, DDD)
# EEE = (EEE, EEE)
# GGG = (GGG, GGG)
# ZZZ = (ZZZ, ZZZ)"""
# ## 6 steps
# RAW = """LLR

# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)"""
### 6 steps
# RAW = """LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)"""
print(RAW)

def parse_raw():
    instructions, network = RAW.split("\n\n")
    net = {}
    for line in network.splitlines():
        src, dsts = line.split(" = ")
        net[src] = dsts.lstrip("(").rstrip(")").split(", ")
    return instructions, net

DATA = parse_raw()
print("DATA")
print(DATA)

import itertools
def part_one():
    counter = 0
    curr_pos = "AAA"
    cycle = itertools.cycle(DATA[0])
    curr_instr = next(cycle)
    while curr_pos != "ZZZ":
        if curr_instr == "L":
            curr_pos = DATA[1][curr_pos][0]
        elif curr_instr == "R":
            curr_pos = DATA[1][curr_pos][1]
        curr_instr = next(cycle)
        counter += 1
    return counter

import math
def part_two():
    counter = 0
    positions = [x for x in DATA[1].keys() if x[2] == "A"]
    first_z = [0] * len(positions)
    cycle = itertools.cycle(DATA[0])
    curr_instr = next(cycle)
    while any(z == 0 for z in first_z):
        for i, pos in enumerate(positions):
            if pos[-1] == "Z":
                first_z[i] = counter if not first_z[i] else first_z[i]
                continue
            if curr_instr == "L":
                positions[i] = DATA[1][pos][0]
            elif curr_instr == "R":
                positions[i] = DATA[1][pos][1]
        curr_instr = next(cycle)
        counter += 1
    ans = math.lcm(*first_z)
    return ans

aoc_lube.submit(year=2023, day=8, part=1, solution=part_one)
aoc_lube.submit(year=2023, day=8, part=2, solution=part_two)
