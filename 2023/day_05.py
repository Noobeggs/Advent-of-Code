import aoc_lube

RAW = aoc_lube.fetch(year=2023, day=5)
# RAW = """seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4"""
print(RAW)

import collections
def parse_raw():
    seeds, info = RAW.split("\n\n", 1)
    my_seeds = seeds.removeprefix("seeds: ").split()
    categories = info.split("\n\n")
    maps = [collections.defaultdict(lambda:-1) for x in range(len(categories))]
    for cati, cat in enumerate(categories):
        # print("h9i")
        # print(cat)
        # print("inbetween")
        map_ranges = cat.split("\n", 1)[1]
        # print(map_ranges)
        lines = map_ranges.splitlines()
        # print(f"lines: {lines}")
        for line in lines:
            l = line.split()
            dst = int(l[0])
            src = int(l[1])
            rng = int(l[2])
            ### DO NOT RUN THE TWO LINES BELOW ON REAL INPUT UNLESS YOU WANT YOUR PC TO CRASH AHAHAHA
            # for i in range(src, src+rng):
            #     maps[cati][src+i-src] = dst+i-src
            maps[cati][(src, src+rng-1)] = dst
    return my_seeds, maps

DATA = parse_raw()

def part_one():
    min_loc = 9999999999999999999999
    for seed in DATA[0]:
        src = int(seed)
        # print(src)
        for map in DATA[1]:
            # print(src, map[src])
            for k, v in map.items():
                if k[0] <= src <= k[1]:
                    src = v + src - k[0]
                    break
            
        # print(f"src: {src}")
        min_loc = min(src, min_loc)
    return min_loc

def check_map(mapping, seeds):
    ### EDIT: seeds and k are first_seed, last_seed... the same as in parse_raw() function
    dst = []
    newseeds = [seeds]
    while newseeds:
        currseeds = newseeds.pop() ### Might as well spell it as "cursed" LOL
        if currseeds[0] > currseeds[1]:
            print("gdi noobeggs you dumbass")
            exit()
        for k, v in mapping.items():
            if k[0] <= currseeds[0] <= k[1]:
                ### starts within a range, might end within a range, or it might not
                # print("k0k1v, starts in range")
                # print(k[0], k[1], v)
                first_dst = currseeds[0] + v - k[0]
                if currseeds[1] <= k[1]:
                    ### Within range of the key in the map
                    dst.append((first_dst, currseeds[1] + v - k[0]))
                else:
                    ### last_seed is out of range...
                    ### cut off the first key in the map from seeds and recursively get the ranges of all dst ranges
                    end_dst = k[1] + v - k[0]
                    dst.append((first_dst, end_dst))
                    newseeds.append((k[1] + 1, currseeds[1]))
                    # dst += check_map(mapping, (end_dst + 1, currseeds[1])) ### Lets use our own stack just in case there's not enough stack memory
                break ### Continue with either the cut off seed range or just end if the seed's range is between the key's range
            elif k[0] <= currseeds[1] <= k[1]:
                ### ends within a range
                # print("k0k1v, ends in range")
                # print(k[0], k[1], v)
                newseeds.append((currseeds[0], k[0]-1))
                dst.append((v, currseeds[1] + v - k[0]))
                break
            elif currseeds[0] < k[0] < currseeds[1]:
                ### overlaps a range, k[1] < currseeds[1] is implied due to earlier checks
                # print("k0k1v, seeds overlap range")
                # print(k[0], k[1], v)
                dst.append((v, v + k[1] - k[0]))
                newseeds.append((currseeds[0], k[0]-1)) # Cut off the beginning
                newseeds.append((k[1] + 1, currseeds[1])) # Cut off the end
                break
        else:
            ### Is not in any range, map it to itself
            dst.append((currseeds[0], currseeds[1]))
    return dst

def part_two():
    min_loc = 9999999999999999999999
    seeds_str = list(map(int, DATA[0]))
    seeds = list(zip(seeds_str, seeds_str[1:]))[::2]
    src = list(map(lambda x: (x[0], x[0] + x[1] - 1), seeds))
    dst = []
    for maps in DATA[1]:
        if dst:
            ### Use last maps dst as this maps src
            src = dst
            dst = []
        for first, last in src:
            dst += check_map(maps, (first, last))
    else:
        first_dsts = list(map(lambda x: x[0], dst))
        min_loc = min(min_loc, min(first_dsts))
    return min_loc

print(part_two())

aoc_lube.submit(year=2023, day=5, part=1, solution=part_one)
aoc_lube.submit(year=2023, day=5, part=2, solution=part_two) #37806486
