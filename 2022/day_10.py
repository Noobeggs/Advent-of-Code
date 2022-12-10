import aoc_lube

RAW = aoc_lube.fetch(year=2022, day=10)
# RAW = """addx 15
# addx -11
# addx 6
# addx -3
# addx 5
# addx -1
# addx -8
# addx 13
# addx 4
# noop
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx -35
# addx 1
# addx 24
# addx -19
# addx 1
# addx 16
# addx -11
# noop
# noop
# addx 21
# addx -15
# noop
# noop
# addx -3
# addx 9
# addx 1
# addx -3
# addx 8
# addx 1
# addx 5
# noop
# noop
# noop
# noop
# noop
# addx -36
# noop
# addx 1
# addx 7
# noop
# noop
# noop
# addx 2
# addx 6
# noop
# noop
# noop
# noop
# noop
# addx 1
# noop
# noop
# addx 7
# addx 1
# noop
# addx -13
# addx 13
# addx 7
# noop
# addx 1
# addx -33
# noop
# noop
# noop
# addx 2
# noop
# noop
# noop
# addx 8
# noop
# addx -1
# addx 2
# addx 1
# noop
# addx 17
# addx -9
# addx 1
# addx 1
# addx -3
# addx 11
# noop
# noop
# addx 1
# noop
# addx 1
# noop
# noop
# addx -13
# addx -19
# addx 1
# addx 3
# addx 26
# addx -30
# addx 12
# addx -1
# addx 3
# addx 1
# noop
# noop
# noop
# addx -9
# addx 18
# addx 1
# addx 2
# noop
# noop
# addx 9
# noop
# noop
# noop
# addx -1
# addx 2
# addx -37
# addx 1
# addx 3
# noop
# addx 15
# addx -21
# addx 22
# addx -6
# addx 1
# noop
# addx 2
# addx 1
# noop
# addx -10
# noop
# noop
# addx 20
# addx 1
# addx 2
# addx 2
# addx -6
# addx -11
# noop
# noop
# noop"""
print(RAW)

def parse_raw():
    return RAW.splitlines()

DATA = parse_raw()

def part_one():
    cycle = 0
    x = 1
    ans = 0
    for line in DATA:
        instruction = line.split()
        cycle += 1
        if cycle % 40 == 20:
            print("signal", cycle, x, cycle*x)
            ans += cycle * x
        if instruction[0] == "addx":
            cycle += 1
            if cycle % 40 == 20:
                print("signal addx", instruction[1], cycle, x, cycle*x)
                ans += cycle * x
            x += int(instruction[1])
            print("part one test", x)
        
    print("ans:", ans)
    return ans

# ans = part_one()

def part_two():
    cycle = 0
    x = 1
    ans = [""] * 6
    for line in DATA:
        instruction = line.split()
        row = cycle // 40
        if abs(cycle % 40 - x) > 1:
            print("test", x, cycle)
            ans[row] += "."
        else:
            print("test", x, cycle)
            ans[row] += "#"
        cycle += 1
        if instruction[0] == "addx":
            row = cycle // 40
            if abs(cycle % 40 - x) > 1:
                print("test", x, cycle)
                ans[row] += "."
            else:
                print("test", x, cycle)
                ans[row] += "#"
            cycle += 1
            x += int(instruction[1])

    for line in ans:
        print(line)
    

aoc_lube.submit(year=2022, day=10, part=1, solution=part_one)
aoc_lube.submit(year=2022, day=10, part=2, solution=part_two)