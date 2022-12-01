'''
Referenced from r/adventofcode
'''

with open('input.txt') as file:
    lines = [int(line) for line in file.readlines()]

print(sum(b > a for a, b in zip(lines, lines[1:])))

windows = [sum(window) for window in zip(lines, lines[1:], lines[2:])]

print(sum(b > a for a, b in zip(windows, windows[1:])))