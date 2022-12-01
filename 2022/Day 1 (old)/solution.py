most_calories = -1
current = 0

with open("input.txt") as f:
    for line in f:
        if line.isspace():
            most_calories = current if current > most_calories else most_calories
            current = 0
        else:
            current += int(line)

print(most_calories)

# Part 2

with open("input.txt") as f:
    input = f.read().split("\n\n")

answer = sorted(map(lambda x: sum(map(int, x.split("\n"))), input))
print(answer[-1], answer[-2], answer[-3])
print(sum(answer[-3:]))