import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

lines = puzzleinput.lines()

sample = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""
# lines = sample.strip().split("\n")

part1 = 0

g = [list(int(x) for x in y) for y in lines]

start = []
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if g[y][x] == 0:
            start.append((x, y))

def neighbors(x, y):
    return [(x+a,y+b) for a in [-1,0,1] for b in [-1,0,1] if 0 <= x+a < len(g[0]) and 0 <= y+b < len(g) and (a,b) != (0,0) and a+b in [-1,1]]

def validpaths(x,y,c):
    return [(a,b) for a,b in neighbors(x,y) if g[b][a] == c+1]

trails = [set([(s[0],s[1])]) for s in start]

for i in range(9):
    ts = trails.copy()
    trails = []
    for s in ts:
        ns = set()
        for n in s:
            ns.update(validpaths(n[0],n[1],i))
        trails.append(ns)

print(sum([len(x) for x in trails]))

part2 = 0

tracker = {s: 1 for s in start}

for i in range(9):
    ts = tracker.copy()
    tracker = {}
    for s in ts:
        for n in validpaths(s[0],s[1],i):
            if n in tracker:
                tracker[n] += ts[s]
            else:
                tracker[n] = ts[s]

print(sum(tracker.values()))
