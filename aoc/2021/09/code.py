from collections import defaultdict
import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """2199943210
3987894921
9856789892
8767896789
9899965678
"""

sample_answer1 = 15
sample_answer2 = 1134

def process(input):
    return [i.strip() for i in input.splitlines()]

print(process(sample_input))

def neighbors(loc):
    return [(loc[0]+dx, loc[1]+dy) for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]]

def p1(input):
    data = process(input)
    grid = {}
    lows = []
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            grid[(x,y)] = char
    for loc, char in grid.items():
        ns = [grid[n] for n in neighbors(loc) if n in grid]
        lower = [n for n in ns if n <= char]
        if not lower:
            lows.append(char)
    return sum([int(l)+1 for l in lows])

def collect_basin(grid, basin):
    bs = basin.copy()
    for loc in bs:
        ns = [n for n in neighbors(loc) if n in grid]
        if inbasin := [n for n in ns if grid[n] != '9' and n not in basin]:
            basin.update(inbasin)
            collect_basin(grid, basin)

def p2(input):
    data = process(input)
    grid = {}
    lows = []
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            grid[(x,y)] = char
    for loc, char in grid.items():
        ns = [n for n in neighbors(loc) if n in grid]
        lower = [n for n in ns if grid[n] <= char]
        if not lower:
            lows.append(loc)
    basins = [set([l]) for l in lows]
    for b in basins:
        collect_basin(grid, b)

    bs = sorted([len(b) for b in basins])
    return bs[-1] * bs[-2] * bs[-3]

if sample_answer1:
    sample_result = p1(sample_input)
    print("sample1 test", sample_result == sample_answer1)
    print("sample1", sample_result)
    if sample_result == sample_answer1:
        print("\nproblem1", p1(input), "\n\n")
if sample_answer2:
    sample_result = p2(sample_input)
    print("sample2 test", sample_result == sample_answer2)
    print("sample2", sample_result)
    if sample_result == sample_answer2:
        print("\nproblem2", p2(input), "\n\n")
