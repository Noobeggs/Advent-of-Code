import aoc_lube

RAW = aoc_lube.fetch(year=2022, day=7)
print(RAW)

def parse_raw():
    return RAW.split("$ ")

DATA = parse_raw()
# print(DATA)

class Directory_Tree_Node():
    def __init__(self, parent):
        # self.dir_name = dir_name
        self.directories = {}
        self.files_size = 0
        self.parent = parent

    def add_directory(self, dir_name):
        new_dir = Directory_Tree_Node(self)
        self.directories[dir_name] = new_dir
    
    def parse_ls(self, ls_output):
        # print("ls:", ls_output)
        for line in ls_output.splitlines():
            # print("line:", line)
            part1, part2 = line.split()
            # print(part1, part2)
            if part1 == "dir":
                self.add_directory(part2)
            else:
                self.files_size += int(part1)
        self.update_parents(self.files_size)
    
    def update_parents(self, size: int):
        if self.parent:
            self.parent.files_size += size
            self.parent.update_parents(size)

def part_one():
    root = curr = Directory_Tree_Node(None)
    for command in DATA:
        if command[:2] == "cd":
            _, dir = command.split()
            if dir == "..":
                curr = curr.parent
            elif dir == "/":
                curr = root
            else:
                curr = curr.directories.get(dir)
        elif command[:2] == "ls":
            curr.parse_ls(command.split('\n', 1)[1])
            # print(curr.directories.keys())

    # def dfs(dir: Directory_Tree_Node):
    #     size = dir.files_size
    #     sum = 0
    #     for d in dir.directories.values():
    #         d_size, d_sum = dfs(d)
    #         size += d_size
    #         sum += d_sum
        
    #     if size <= 100_000:
    #         sum += size
    #     return size, sum
    
    # size, sum = dfs(root)
    # return sum

    def dfs(dir: Directory_Tree_Node):
        sum = 0
        for d in dir.directories.values():
            d_sum = dfs(d)
            sum += d_sum
        
        if dir.files_size <= 100_000:
            sum += dir.files_size
        return sum
    sum = dfs(root)
    print("root_size:", root.files_size)
    print("Part 1:", sum)
    return sum

test = part_one()

def part_two():
    # Same as part_one
    root = curr = Directory_Tree_Node(None)
    for command in DATA:
        if command[:2] == "cd":
            _, dir = command.split()
            if dir == "..":
                curr = curr.parent
            elif dir == "/":
                curr = root
            else:
                curr = curr.directories.get(dir)
        elif command[:2] == "ls":
            curr.parse_ls(command.split('\n', 1)[1])
            # print(curr.directories.keys())

    '''
    PRESERVING MY DESIGN MISTAKES T^T
    '''
    # # different dfs logic from part_one
    # def dfs(dir: Directory_Tree_Node):
    #     size = dir.files_size
    #     # sum = 0
    #     for d in dir.directories.values():
    #         d_size, d_sum = dfs(d)
    #         size += d_size
    #         # sum += d_sum
        
    #     # if size <= 100_000:
    #     #     sum += size
    #     return size
    
    # size = dfs(root)
    # min_to_delete = 30_000_000 - (70_000_000 - size)

    # # I'm doing this 2 times, which isn't quite optimal...
    # # Probably could memoize/cache the directory sizes...
    # # Maybe do it while building the Tree, so I don't have to to all this recursive bullshit XD
    # # TODO: Implement my ideas above.
    # def dfs2(dir: Directory_Tree_Node):

    # min_dir_size_to_del = 

    def dfs(dir: Directory_Tree_Node, min_to_delete: int):
        min_dir_size_to_del = 30_000_000
        for d in dir.directories.values():
            min = dfs(d, min_to_delete)
            if min_to_delete <= min < min_dir_size_to_del:
                min_dir_size_to_del = min
        if min_to_delete <= dir.files_size < min_dir_size_to_del:
            min_dir_size_to_del = dir.files_size

        return min_dir_size_to_del

    print("how big is this lol:", root.files_size)
    min_to_delete = 30_000_000 - (70_000_000 - root.files_size)
    print("help me:", min_to_delete)
    return dfs(root, min_to_delete)


aoc_lube.submit(year=2022, day=7, part=1, solution=part_one)
aoc_lube.submit(year=2022, day=7, part=2, solution=part_two)