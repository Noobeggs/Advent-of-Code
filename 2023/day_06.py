import aoc_lube

RAW = aoc_lube.fetch(year=2023, day=6)
print(RAW)

def parse_raw():
    time, distance = RAW.splitlines()
    ttitle, times = time.split(":")
    dtitle, dists = distance.split(":")
    return times.lstrip().split(), dists.lstrip().split()

DATA = parse_raw()
print(DATA)

def part_one():
    prod = 0
    for i, races in enumerate(list(zip(*DATA))):
        print(i, races)
        waystowin = 0
        t = int(races[0])
        d = int(races[1])
        for x in range(t+1):
            if (t-x) * x > d:
                waystowin += 1
        prod = prod * waystowin if prod else waystowin
    return prod
        
def part_two():
    ans = 0
    time, dist = "", ""
    for ts in DATA[0]:
        time += ts
    t = int(time)
    for ds in DATA[1]:
        dist += ds
    d = int(dist)

    for x in range(t+1):
        if (t-x) * x > d:
            ans += 1
    return ans

aoc_lube.submit(year=2023, day=6, part=1, solution=part_one)
aoc_lube.submit(year=2023, day=6, part=2, solution=part_two)
