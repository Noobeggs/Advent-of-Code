import aoc_lube

RAW = aoc_lube.fetch(year=2023, day=4)
# RAW = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
print(RAW)

def parse_raw():
    return RAW.splitlines()
    # card_no, numbers = lines.split(": ")
    # winning_numbers, numbers_i_have = numbers.split(" | ")
    # return winning_numbers, numbers_i_have

DATA = parse_raw()

def part_one():
    sum = 0
    for line in DATA:
        score = 0
        card_no, numbers = line.split(": ")
        winning_numbers, numbers_i_have = numbers.split(" | ")
        print(winning_numbers, numbers_i_have)
        wnum = set(winning_numbers.split())
        nih = set(numbers_i_have.split())
        winning_i_have = wnum & nih
        print(winning_i_have)
        if winning_i_have:
            score = 2 ** (len(winning_i_have) - 1)
        print(score)
        sum += score
    return sum

import collections
def part_two():
    # sum = 0
    cards = collections.defaultdict(lambda:0)
    for i, line in enumerate(DATA):
        cards[i+1] += 1
        card_no, numbers = line.split(": ")
        winning_numbers, numbers_i_have = numbers.split(" | ")
        wnum = set(winning_numbers.split())
        nih = set(numbers_i_have.split())
        winning_i_have = wnum & nih
        if winning_i_have:
            # print(len(winning_i_have), copies)
            # sum += len(winning_i_have) * copies
            for x in range(len(winning_i_have)):
                cards[i+2+x] += 1 * cards[i+1]
                print(i+2+x, cards[i+2+x])
    print(cards.values())
    return sum(cards.values())


aoc_lube.submit(year=2023, day=4, part=1, solution=part_one)
aoc_lube.submit(year=2023, day=4, part=2, solution=part_two)
