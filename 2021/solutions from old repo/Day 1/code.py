from collections import deque

prev, count = 0, 0

with open('input.txt') as f:
# with open('test.txt') as f:
    for line in f:
        if not prev:
            prev = int(line)
        else:
            curr = int(line)
            if curr > prev:
                count += 1
            prev = int(line)

print(count)

prev, count = 0, 0
window = deque()
with open('input.txt') as f:
# with open('test.txt') as f:
    for line in f:
        if len(window) < 3:
            window.append(int(line))
            continue
        elif not prev:
            prev = sum(window)

        window.popleft()
        window.append(int(line))
        curr = sum(window)
        if curr > prev:
            count += 1
        prev = curr

print(count)