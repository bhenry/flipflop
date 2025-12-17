from collections import defaultdict
from copy import deepcopy
import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#
"""

sample_answer1 = 18
sample_answer2 = 54

def process(input):
    return [i.strip() for i in input.splitlines()]

def left(loc, width):
    if loc[0]-1 <= 0:
        return (width-2, loc[1])
    return (loc[0]-1, loc[1])
def right(loc, width):
    if loc[0]+1 >= width-1:
        return (1, loc[1])
    return (loc[0]+1, loc[1])
def up(loc, height):
    if loc[1]-1 <= 0:
        return (loc[0], height-2)
    return (loc[0], loc[1]-1)
def down(loc, height):
    if loc[1]+1 >= height-1:
        return (loc[0], 1)
    return (loc[0], loc[1]+1)

def p1(input):
    data = process(input)
    grid = defaultdict(list)
    width = len(data[0])
    height = len(data)
    for y, row in enumerate(data):
        for x, col in enumerate(row):
            if col != '.':
                grid[(x,y)].append(col)
    store = set()
    store.add((1,0)) # start at (1,0)
    minute = 0
    start = (1,0)
    finish = (width-2, height-1)
    moves = [(0,0), (0,1), (1,0), (0,-1), (-1,0)]
    while True:
        minute += 1
        copy = deepcopy(grid)
        for loc, val in copy.items():
            for v in val:
                if v == '<':
                    grid[left(loc, width)].append('<')
                    grid[loc].remove('<')
                if v == '>':
                    grid[right(loc, width)].append('>')
                    grid[loc].remove('>')
                if v == '^':
                    grid[up(loc, height)].append('^')
                    grid[loc].remove('^')
                if v == 'v':
                    grid[down(loc, height)].append('v')
                    grid[loc].remove('v')
        paths = set()
        for path in store:
            validnexts = set()
            for move in moves:
                dest = (path[0] + move[0], path[1] + move[1])
                if dest == finish:
                    print("you win")
                    print("minute", minute)
                    print("path", path)
                    print("dest", dest)
                    return minute
                if dest == start:
                    validnexts.add(dest)
                if dest[0] <= 0 or dest[0] >= width-1 or dest[1] <= 0 or dest[1] >= height-1:
                    continue
                if grid.get(dest) == []:
                    validnexts.add(dest)
            for next in validnexts:
                paths.add(next)
        store = paths


def p2(input):
    data = process(input)
    grid = defaultdict(list)
    width = len(data[0])
    height = len(data)
    for y, row in enumerate(data):
        for x, col in enumerate(row):
            if col != '.':
                grid[(x,y)].append(col)
    store = set()
    store.add(((1,0), False, False)) # start at (1,0), reached finish, reached start
    minute = 0
    start = (1,0)
    finish = (width-2, height-1)
    moves = [(0,0), (0,1), (1,0), (0,-1), (-1,0)]
    while True:
        minute += 1
        copy = deepcopy(grid)
        for loc, val in copy.items():
            for v in val:
                if v == '<':
                    grid[left(loc, width)].append('<')
                    grid[loc].remove('<')
                if v == '>':
                    grid[right(loc, width)].append('>')
                    grid[loc].remove('>')
                if v == '^':
                    grid[up(loc, height)].append('^')
                    grid[loc].remove('^')
                if v == 'v':
                    grid[down(loc, height)].append('v')
                    grid[loc].remove('v')
        paths = set()
        for key in store:
            path, reached_finish, reached_start = key
            validnexts = set()
            for move in moves:
                dest = (path[0] + move[0], path[1] + move[1])
                if dest == finish and reached_start:
                    return minute
                if dest == finish:
                    validnexts.add((dest, True, False))
                if dest == start and reached_finish:
                    validnexts.add((dest, True, True))
                if dest[0] < 0 or dest[0] >= width or dest[1] < 0 or dest[1] >= height:
                    continue
                if not grid.get(dest):
                    validnexts.add((dest, reached_finish, reached_start))
            for next in validnexts:
                paths.add(next)
        store = paths

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
