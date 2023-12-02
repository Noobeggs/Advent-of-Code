import aoc_lube

RAW = aoc_lube.fetch(year=2023, day=2)
# RAW = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
print(RAW)

def parse_raw():
    return RAW.splitlines()

DATA = parse_raw()

def part_one():
    sum = 0
    for i, line in enumerate(DATA):
        valid = True
        game_no, xd = line.split(": ")
        for set_no in xd.split("; "):
            blue = 0
            red = 0
            green = 0
            for ball in set_no.split(", "):
                x = ball.split(" ")
                # print(x)
                if x[1] == "blue":
                    blue += int(x[0])
                elif x[1] == "red":
                    red += int(x[0])
                elif x[1] == "green":
                    green += int(x[0])
            if blue <= 14 and red <= 12 and green <= 13:
                print(blue, red, green)
                continue
            else:
                valid = False
                break
        if valid:
            print(i)
            sum += i + 1

    return sum


def part_two():
    sum = 0
    for i, line in enumerate(DATA):
        min_r = min_g = min_b = 0
        game_no, xd = line.split(": ")
        for set_no in xd.split("; "):
            blue = 0
            red = 0
            green = 0
            for ball in set_no.split(", "):
                x = ball.split(" ")
                # print(x)
                if x[1] == "blue":
                    blue += int(x[0])
                elif x[1] == "red":
                    red += int(x[0])
                elif x[1] == "green":
                    green += int(x[0])
            min_b = max(min_b, blue)
            min_r = max(min_r, red)
            min_g = max(min_g, green)
        sum += min_r*min_g*min_b
    return sum

aoc_lube.submit(year=2023, day=2, part=1, solution=part_one)
aoc_lube.submit(year=2023, day=2, part=2, solution=part_two)
