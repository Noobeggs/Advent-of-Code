'''
PART ONE
'''

horizontal, depth = 0, 0

with open('input.txt') as file:
# with open('test.txt') as file:
    for line in file:
        command, distance = line.split()

        if command == "forward":
            horizontal += int(distance)
        elif command == "down":
            depth += int(distance)
        elif command == "up":
            depth -= int(distance)

print(horizontal * depth)

'''
PART TWO
'''

horizontal, depth, aim = 0, 0, 0

with open('input.txt') as file:
# with open('test.txt') as file:
    for line in file:
        command, distance = line.split()

        if command == "forward":
            horizontal += int(distance)
            depth += aim * int(distance)
        elif command == "down":
            aim += int(distance)
        elif command == "up":
            aim -= int(distance)

print(horizontal * depth)