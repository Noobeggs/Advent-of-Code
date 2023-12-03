import aoc_lube

RAW = aoc_lube.fetch(year=2023, day=3)
# RAW = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
# """
print(RAW)

def parse_raw():
    return [list(x) for x in RAW.splitlines()]

DATA = parse_raw()
# print(DATA)

def search(x, y, max_x, max_y):
    around = [(x, y)]
    if x < max_x and y < max_y:
        around.append((x+1, y+1))
    if x < max_x and y > 0:
        around.append((x+1, y-1))
    if x < max_x:
        around.append((x+1, y))
    if y < max_y and x > 0:
        around.append((x-1, y+1))
    if y < max_y:
        around.append((x, y+1))
    if x > 0 and y > 0:
        around.append((x-1, y-1))
    if x > 0:
        around.append((x-1, y))
    if y > 0:
        around.append((x, y-1))
    # print(around)
    return around

def is_number(x):
    return x in "0123456789"

def is_symbol(x):
    return x not in "1234567890."

# def part_one():
#     x_len = len(DATA[0])
#     y_len = len(DATA)
#     parts = {0}
#     sum = 0
#     for y, line in enumerate(DATA):
#         is_num = False
#         has_symbol = False
#         int_str = ""
#         for x, c in enumerate(line):
#             if is_number(c) and x != x_len-1 and is_num:
#                 # Continuation of number, not last column
#                 int_str += c
#             elif is_number(c) and not is_num:
#                 # Start of new number
#                 is_num = True
#                 int_str = c
#             # elif c.isdigit() and is_num and has_symbol:
#             #     int_str += c
#             elif ((x == x_len-1 and is_number(c)) or not is_number(c)) and is_num and has_symbol:
#                 # End of number or line, update parts
#                 is_num = x == x_len-1 and is_number(c)
#                 has_symbol = False if not is_number(c) else has_symbol
#                 print(int_str)
#                 # print(y, x)
#                 # parts.add(int(int_str))
#                 sum += int(int_str)
#                 int_str = ""
#             elif not is_number(c):
#                 # Not number string, reset just in case
#                 is_num = False
#                 has_symbol = False
#                 int_str = ""
#             if is_num and not has_symbol:
#                 # Is number, Find symbols
#                 adjacents = search(x, y, x_len-1, y_len-1)
#                 for adj in adjacents:
#                     point = DATA[adj[1]][adj[0]]
#                     if point != "." and not point.isnumeric():
#                         has_symbol = True
#                         break
#                 if x == x_len-1:
#                     # if last column lol
#                     # parts.add(int(int_str))
#                     sum += int(int_str)
#     return sum #519922 WRONG 323955 WRONG 324015 WRONG 520224 WRONG

def part_one():
    #JUST FML MAN WTF, WHY AM I SO STUBBORN LOL, IF I CHANGED APPROACH EARLIER WOULD'VE BEEN WAY FASTER zzz
    parts = {}
    x_len = len(DATA[0])
    y_len = len(DATA)
    for y, line in enumerate(DATA):
        for x, c in enumerate(line):
            if is_symbol(c):
                adjacents = search(x, y, x_len-1, y_len-1)
                for adj in adjacents:
                    xt = adj[0]
                    yt = adj[1]
                    point = DATA[yt][xt]
                    if is_number(point):
                        while xt > 0 and is_number(DATA[yt][xt-1]):
                            xt -= 1
                        num_start = (xt, yt)
                        int_str = ""
                        while xt < x_len and is_number(DATA[yt][xt]):
                            int_str += DATA[yt][xt]
                            xt += 1
                        parts[num_start] = int(int_str)
    return sum(parts.values())


def part_two():
    gears = {}
    x_len = len(DATA[0])
    y_len = len(DATA[1])
    gear_ratios = 0
    for y, line in enumerate(DATA):
        for x, c in enumerate(line):
            if c == "*":
                numbers = set()
                adjacents = search(x, y, x_len-1, y_len-1)
                for adj in adjacents:
                    xt = adj[0]
                    yt = adj[1]
                    point = DATA[yt][xt]
                    if is_number(point):
                        while xt > 0 and is_number(DATA[yt][xt-1]):
                            xt -= 1
                        num_start = (xt, yt)
                        int_str = ""
                        while xt < x_len and is_number(DATA[yt][xt]):
                            int_str += DATA[yt][xt]
                            xt += 1
                        # print(int_str)
                        numbers.add(num_start)
                        gears[num_start] = int(int_str)
                if len(numbers) == 2:
                    print(numbers)
                    product = 1
                    for nums in numbers:
                        product *= gears[nums]
                    gear_ratios += product
    return gear_ratios
                        

aoc_lube.submit(year=2023, day=3, part=1, solution=part_one)
aoc_lube.submit(year=2023, day=3, part=2, solution=part_two)
