import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

sample_answer1 = 95437
sample_answer2 = 24933642

def process(input):
    data = [i.strip() for i in input.splitlines()]
    dirs = {"/": 0}
    path = []
    for line in data:
        if line.startswith("$ cd .."):
            path.pop()
        elif line.startswith("$ cd "):
            path.append(line.split()[2])
        elif line[0].isdigit():
            size = int(line.split()[0])
            for parts in range(len(path)):
                p = "/".join(path[:parts+1])
                if dirs.get(p):
                    dirs[p] += size
                else:
                    dirs[p] = size
    return dirs

def p1(input):
    dirs = process(input)
    return sum([dirs[d] for d in dirs if dirs[d] < 100000])

def p2(input):
    dirs = process(input)
    possible = []
    for d in dirs:
        if 70000000 - (dirs["/"] - dirs[d]) > 30000000:
            possible.append(dirs[d])
    return min(possible)

if sample_answer1:
    print("sample test", p1(sample_input) == sample_answer1)
    print("Problem1", p1(input))
if sample_answer2:
    print("sample test2", p2(sample_input) == sample_answer2)
    print("Problem2", p2(input))
