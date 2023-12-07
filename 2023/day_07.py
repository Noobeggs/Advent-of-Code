import aoc_lube

RAW = aoc_lube.fetch(year=2023, day=7)
# RAW = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483"""
print(RAW)

def parse_raw():
    return [x.split() for x in RAW.splitlines()]

DATA = parse_raw()
print(DATA)

import collections
def check_hand(hand):
    unique = collections.Counter(hand)
    if len(unique) == 1:
        # Five of a kind
        return 7
    if len(unique) == 2:
        # Four oak or FH
        return 6 if unique.most_common(1)[0][1] == 4 else 5
    if len(unique) == 3:
        # Three oak or 2P
        return 4 if unique.most_common(1)[0][1] == 3 else 3
    if len(unique) == 4:
        # 1P
        return 2
    if len(unique) == 5:
        # High card
        return 1
    
def part_one():
    sum = 0
    ranks = collections.defaultdict(list)
    hands_len = len(DATA)
    for hand, bid in DATA:
        rank = check_hand(hand)
        ranks[rank].append((hand, int(bid)))

    labels = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(", ")
    label_order = {v: k for k, v in enumerate(labels)}

    counter = 1
    for x in range(1, 8):
        ranks[x].sort(key=lambda val: (label_order[val[0][0]], label_order[val[0][1]], label_order[val[0][2]], label_order[val[0][3]], label_order[val[0][4]]), reverse=True)
        for hand in ranks[x]:
            sum += hand[1] * counter
            counter += 1
    return sum
        
def check_hand_joker_rule(hand):
    unique = collections.Counter(hand)
    if len(unique) == 1:
        # Five of a kind
        return 7
    if len(unique) == 2:
        # Four oak or FH
        if unique["J"]:
            return 7 #All combinations lead to 5 oak
        else:
            return 6 if unique.most_common(1)[0][1] == 4 else 5
    if len(unique) == 3:
        # Three oak or 2P
        jokers = unique["J"]
        if jokers:
            if jokers == 3:
                return 6 #4 oak from 3 oak
            if jokers == 2:
                return 6 #4 oak from 2P
            if jokers == 1:
                return 6 if unique.most_common(1)[0][1] == 3 else 5 #4 oak if 3 oak, FH if 2P
        return 4 if unique.most_common(1)[0][1] == 3 else 3
    if len(unique) == 4:
        # 1P
        if unique["J"]:
            return 4 #All combis lead to 3 oak
        return 2
    if len(unique) == 5:
        # High card
        if unique["J"]:
            return 2 #2P
        return 1

def part_two():
    sum = 0
    ranks = collections.defaultdict(list)
    labels = "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".split(", ")
    label_order = {v: k for k, v in enumerate(labels)}
    for hand, bid in DATA:
        rank = check_hand_joker_rule(hand)
        ranks[rank].append((hand, int(bid)))
    
    counter = 1
    for x in range(1, 8):
        ranks[x].sort(key=lambda val: (label_order[val[0][0]], label_order[val[0][1]], label_order[val[0][2]], label_order[val[0][3]], label_order[val[0][4]]), reverse=True)
        for hand in ranks[x]:
            sum += hand[1] * counter
            counter += 1
    return sum

aoc_lube.submit(year=2023, day=7, part=1, solution=part_one)
aoc_lube.submit(year=2023, day=7, part=2, solution=part_two)
