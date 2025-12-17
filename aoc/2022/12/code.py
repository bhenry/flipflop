import os
from collections import defaultdict
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""

sample_answer1 = 31
sample_answer2 = 29

def neighbors(loc):
    return [(loc[0]+dx, loc[1]+dy) for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]]

def process(input):
    grid = defaultdict(str)
    for i, r in enumerate(input.splitlines()):
        for c in range(len(r)):
            grid[(i,c)] = r[c]
            if r[c] == 'E':
                dest = (i,c)
            if r[c] == 'S':
                start = (i,c)
    return grid, dest, start

def step(grid, loc, start=None):
    new_points = set()
    for point in neighbors(loc):
        curheight = ord(grid[loc])
        curheight = ord('z') if grid[loc] == 'E' else curheight
        curheight = ord('a') if grid[loc] == 'S' else curheight
        neighborheight = ord(grid[point]) if grid[point] else -100
        neighborheight = ord('z') if grid[point] == 'E' else neighborheight
        neighborheight = ord('a') if grid[point] == 'S' else neighborheight
        if curheight - neighborheight in [1, 0] or curheight < neighborheight:
            if not start and curheight == ord('a'):
                return "DONE"
            new_points.add(point)
    return new_points # the options we can go to in this step

def p1(input):
    grid, dest, start = process(input)
    rounds = 1
    visited = set([dest])
    new_options = step(grid, dest, start) - visited
    visited.update(new_options)
    for _ in range(10000):
        rounds += 1
        temp_options = set()
        for option in new_options:
            temp_options.update(step(grid, option, start))
        new_options = temp_options - visited
        if start in new_options:
            return rounds
        visited.update(new_options)

def p2(input):
    grid, dest, _ = process(input)
    rounds = 0
    visited = set([dest])
    new_options = step(grid, dest) - visited
    visited.update(new_options)
    for _ in range(10000):
        rounds += 1
        temp_options = set()
        for option in new_options:
            next_step = step(grid, option)
            if "DONE" == next_step:
                return rounds
            temp_options.update(next_step)
        new_options = temp_options - visited
        visited.update(new_options)

if sample_answer1:
    sample_result = p1(sample_input)
    print("sample1 test", sample_result == sample_answer1)
    print("sample1", p1(sample_input))
    print("Problem1", p1(input), "\n\n")
if sample_answer2:
    sample_result = p2(sample_input)
    print("sample2 test", sample_result == sample_answer2)
    print("sample2", p2(sample_input))
    print("Problem2", p2(input))
