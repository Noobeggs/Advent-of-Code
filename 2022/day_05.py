import aoc_lube

RAW = aoc_lube.fetch(year=2022, day=5)
print(RAW)

def parse_raw():
    '''
        THIS WAS AN ABSOLUTE NIGHTMARE TO PARSE LOL!
        HARDCODING THE INPUT INTO MY CODE WOULD'VE TAKEN ME WAY LESS TIME XDDDD
    '''
    stacks, commands = RAW.split("\n\n")
    
    stacks = stacks.splitlines()
    # print("test", stacks)
    # print(list(zip(*stacks)))
    stacks = ["".join(line[::-1][1:]).strip() for line in zip(*stacks) if line[-1].isdigit()]
    # for stack in stacks:
    #     for crate in stack:
    parsed_stacks = []
    for num, stack in enumerate(stacks):
        parsed_stacks.append([])
        for crate in stack:
            parsed_stacks[num].append(crate)
            
    # parsed_stacks = []
    # for col in zip(*stacks):
    #     if col[-1].isdigit():
    #         parsed_stacks.append([])
    #         for char in col:
    #             if not char.isspace():
    #                 parsed_stacks

    # parsed_commands = []
    # for line in commands.splitlines():
    #     line1 = line.split()
    #     print(line1)
    #     line2 = filter(str.isdigit, line1)
    #     # print(xd for xd in line2)
    #     line3 = map(int, line2)
    #     line4 = list(line3)
    #     parsed_commands.append(line4)

    parsed_commands = [list(map(int, filter(str.isdigit, line.split()))) for line in commands.splitlines()]
    # print("test commands", parsed_commands)

    return parsed_stacks, parsed_commands

STACKS, COMMANDS = parse_raw()

print(STACKS)
# print(COMMANDS)

def part_one():
    end = ""
    for step in COMMANDS:
        # print("step:", step)
        for _ in range(step[0]):
            # print(step[2]-1)
            # print("from:", STACKS[step[1]-1])
            # print("to:", STACKS[step[2]-1])
            STACKS[step[2]-1].append(STACKS[step[1]-1].pop())

    print(STACKS)
    for stack in STACKS:
        end += stack[-1]
    return end

def part_two():
    end = ""
    for step in COMMANDS:
        temp = []
        for _ in range(step[0]):
            temp.append(STACKS[step[1]-1].pop())
        for crate in temp[::-1]:
            STACKS[step[2]-1].append(crate)
    
    for stack in STACKS:
        end += stack[-1]
    return end

aoc_lube.submit(year=2022, day=5, part=1, solution=part_one)
aoc_lube.submit(year=2022, day=5, part=2, solution=part_two)