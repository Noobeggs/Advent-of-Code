import aoc_lube
from collections import deque
from math import lcm

RAW = aoc_lube.fetch(year=2022, day=11)
# RAW = """Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3

# Monkey 1:
#   Starting items: 54, 65, 75, 74
#   Operation: new = old + 6
#   Test: divisible by 19
#     If true: throw to monkey 2
#     If false: throw to monkey 0

# Monkey 2:
#   Starting items: 79, 60, 97
#   Operation: new = old * old
#   Test: divisible by 13
#     If true: throw to monkey 1
#     If false: throw to monkey 3

# Monkey 3:
#   Starting items: 74
#   Operation: new = old + 3
#   Test: divisible by 17
#     If true: throw to monkey 0
#     If false: throw to monkey 1"""
print(RAW)

def parse_raw():
    return RAW.split("\n\n")

DATA = parse_raw()

class Monkey():
    def __init__(self, items, operator, operand, test, true, false) -> None:
        self.items = deque(items)
        self.operator = operator
        self.operand = operand
        self.test = test
        self.true = true
        self.false = false

    def add_item(self, item):
        self.items.append(item)

    def test_worry(self, worry, lcm) -> int:
        if worry % self.test == 0:
            return self.true, worry % lcm
        else:
            return self.false, worry % lcm

    def add(self, worry) -> int:
        if type(self.operand) is int:
            return worry + self.operand
        else:
            return worry + worry

    def multiply(self, worry) -> int:
        if type(self.operand) is int:
            return worry * self.operand
        else:
            return worry ** 2

    def multiply_mod(self, worry) -> int:
        if type(self.operand) is int:
            return (worry % self.test) * (self.operand % self.test)
        else:
            return (worry % self.test) ** 2

    def inspect(self) -> int:
        if self.operator == "+":
            new = self.add(self.items.popleft())
        if self.operator == "*":
            new = self.multiply(self.items.popleft())
        return new // 3

    def inspect_two(self) -> int:
        if self.operator == "+":
            new = self.add(self.items.popleft())
        if self.operator == "*":
            new = self.multiply(self.items.popleft())
        return new
def part_one():
    apes = []
    for monkey in DATA:
        lines = monkey.splitlines()
        line_one = lines[1].split(": ")
        items = map(int, line_one[1].split(", "))
        line_two = lines[2].split(": ")
        formula = line_two[1].split()
        operator = formula[3]
        operand = int(formula[4]) if formula[4].isdigit() else False
        test = int(lines[3].split()[-1])
        if_true = int(lines[4].split()[-1])
        if_false = int(lines[5].split()[-1])

        apes.append(Monkey(items, operator, operand, test, if_true, if_false))
    
    inspect_count = [0] * len(apes)
    for n in range(20):
        print(n)
        for i, monkey in enumerate(apes):
            print("monkey number:", i)
            while monkey.items:
                print(len(monkey.items))
                inspect_count[i] += 1
                worry = monkey.inspect()
                pass_to, item = monkey.test_worry(worry)
                apes[pass_to].add_item(item)

    sorted_count = sorted(inspect_count)
    monkey_business = sorted_count[-1] * sorted_count[-2]
    return monkey_business

def part_two():
    apes = []
    for monkey in DATA:
        lines = monkey.splitlines()
        line_one = lines[1].split(": ")
        items = map(int, line_one[1].split(", "))
        line_two = lines[2].split(": ")
        formula = line_two[1].split()
        operator = formula[3]
        operand = int(formula[4]) if formula[4].isdigit() else False
        test = int(lines[3].split()[-1])
        if_true = int(lines[4].split()[-1])
        if_false = int(lines[5].split()[-1])

        apes.append(Monkey(items, operator, operand, test, if_true, if_false))

    lowest_common_multiple = lcm(*[x.test for x in apes])
    inspect_count = [0] * len(apes)
    for n in range(10000):
        # print(n)
        for i, monkey in enumerate(apes):
            # print("monkey number:", i)
            while monkey.items:
                # print(len(monkey.items))
                inspect_count[i] += 1
                worry = monkey.inspect_two()
                pass_to, item = monkey.test_worry(worry, lowest_common_multiple)
                apes[pass_to].add_item(item)

    sorted_count = sorted(inspect_count)
    monkey_business = sorted_count[-1] * sorted_count[-2]
    print(sorted_count[-1], sorted_count[-2])
    return monkey_business

aoc_lube.submit(year=2022, day=11, part=1, solution=part_one)
aoc_lube.submit(year=2022, day=11, part=2, solution=part_two)