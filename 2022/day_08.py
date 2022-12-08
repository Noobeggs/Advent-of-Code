import aoc_lube

RAW = aoc_lube.fetch(year=2022, day=8)
# RAW = """30373
# 25512
# 65332
# 33549
# 35390"""
print(RAW)

def parse_raw():
    return [list(map(int, tree)) for tree in RAW.splitlines()]

DATA = parse_raw()

def part_one():
    row_len = len(DATA[0])
    col_len = len(DATA)
    ans = col_len * 2 + row_len * 2 - 4
    visible = set()
    for y in range(1, col_len - 1):
        tallest = DATA[y][0]
        for x in range(1, row_len - 1):
            if DATA[y][x] > tallest:
                visible.add((y, x))
                tallest = DATA[y][x]
        
        tallest = DATA[y][row_len - 1]
        for x in range(row_len - 2, 0, -1):
            if DATA[y][x] > tallest:
                visible.add((y, x))
                tallest = DATA[y][x]

    for x in range(1, row_len - 1):
        tallest = DATA[0][x]
        for y in range(1, col_len - 1):
            if DATA[y][x] > tallest:
                visible.add((y, x))
                tallest = DATA[y][x]

        tallest = DATA[col_len - 1][x]
        for y in range(col_len - 2, 0, -1):
            if DATA[y][x] > tallest:
                visible.add((y, x))
                tallest = DATA[y][x]

    ans += len(visible)
    return ans

def part_two():
    row_len = len(DATA[0])
    col_len = len(DATA)
    ans = 0
    for y in range(col_len):
        for x in range(row_len):
            up = down = left = right = 0
            j = y - 1
            while j >= 0:
                up += 1
                if DATA[j][x] >= DATA[y][x]:
                    break
                j -= 1
            j = y + 1
            while j < col_len:
                down += 1
                if DATA[j][x] >= DATA[y][x]:
                    break
                j += 1
            i = x - 1
            while i >= 0:
                left += 1
                if DATA[y][i] >= DATA[y][x]:
                    break
                i -= 1
            i = x + 1
            while i < row_len:
                right += 1
                if DATA[y][i] >= DATA[y][x]:
                    break
                i += 1

            ans = max(ans, up * down * left * right)
            print(x, y)
            print(ans)
    print("ans:", ans)
    return ans

ans = part_two()

aoc_lube.submit(year=2022, day=8, part=1, solution=part_one)
aoc_lube.submit(year=2022, day=8, part=2, solution=part_two)