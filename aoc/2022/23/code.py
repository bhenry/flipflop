from collections import defaultdict
import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..
"""

sample_answer1 = 110
sample_answer2 = 20

def process(input):
    g = {}
    for y, row in enumerate(input.strip().splitlines()):
        for x, val in enumerate(row):
            if val == '#':
                g[(x,y)] = val
    return g

PROPOSALS = [
    # (proposal, list of blockers)
    # if no one is in the list, then we can go to the proposal
    ((0,0), [(0,-1),(0,1),(-1,0),(1,0),(1,-1),(1,1),(-1,-1),(-1,1)]), # stay
    ((0,-1),[(0,-1),(1,-1),(-1,-1)]), # N
    ((0,1),[(0,1),(1,1),(-1,1)]), # S
    ((-1,0),[(-1,0),(-1,1),(-1,-1)]), # W
    ((1,0),[(1,0),(1,1),(1,-1)]), # E
]

def step(grid, proposal_order):
    proposals = {}
    other_proposals = defaultdict(int)
    for x, y in grid:
        for proposal in proposal_order:
            if not any((x+dx,y+dy) in grid for dx,dy in proposal[1]):
                proposals[(x,y)] = (x+proposal[0][0],y+proposal[0][1])
                other_proposals[(x+proposal[0][0],y+proposal[0][1])] +=1
                break
    for k,v in proposals.items():
        if other_proposals[v] == 1:
            grid[v] = '#'
            if k != v:
                del grid[k]
            # print_grid(grid)
    return grid

def stepp(proposals):
    return proposals[0:1] + proposals[2:] + proposals[1:2]

def count_grid(grid):
    minx = min([i[0] for i in grid.keys()])
    maxx = max([i[0] for i in grid.keys()])
    miny = min([i[1] for i in grid.keys()])
    maxy = max([i[1] for i in grid.keys()])
    countup = 0
    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            if not grid.get((x,y)):
                countup += 1
    return countup

def p1(input):
    grid = process(input)
    proposals = PROPOSALS
    for _ in range(10):
        grid = step(grid, proposals)
        proposals = stepp(proposals)
    return count_grid(grid)

def p2(input):
    grid = process(input)
    proposals = PROPOSALS
    turns = 0
    while True:
        newgrid = step(dict(grid), proposals)

        proposals = stepp(proposals)
        turns += 1
        if newgrid == grid:
            break
        grid = newgrid
    return turns

if sample_answer1:
    sample_result = p1(sample_input)
    print("sample1", sample_result)
    if sample_result == sample_answer1:
        print("sample1 test pass")
        print("\nproblem1", p1(input), "\n\n")

if sample_answer2:
    sample_result = p2(sample_input)
    print("sample2", sample_result)
    if sample_result == sample_answer2:
        print("sample2 test pass")
        print("\nproblem2", p2(input), "\n\n")


print("\ndone")
