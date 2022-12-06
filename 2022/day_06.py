import aoc_lube
import collections

RAW = aoc_lube.fetch(year=2022, day=6)
print(RAW)

def parse_raw():
    return RAW

DATA = parse_raw()

def part_one():
    def valid_marker(sequence):
        return len(set(sequence)) == len(sequence) == 4

    counter = 0
    window = collections.deque(maxlen=4)
    for c in DATA:
        window.append(c)
        counter += 1
        if valid_marker(window):
            return counter

def part_two():
    def valid_message_marker(sequence):
        return len(set(sequence)) == len(sequence) == 14

    counter = 0
    window = collections.deque(maxlen=14)
    for c in DATA:
        window.append(c)
        counter += 1
        if valid_message_marker(window):
            return counter

aoc_lube.submit(year=2022, day=6, part=1, solution=part_one)
aoc_lube.submit(year=2022, day=6, part=2, solution=part_two)