import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

lines = puzzleinput.lines()

sample = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
# lines = sample.strip().split("\n")

part1 = 0

g = [line.strip() for line in lines]
w = len(g[0])
h = len(g)

types = {}

for y in range(h):
    for x in range(w):
        if g[y][x] != ".":
            if g[y][x] not in types:
                types[g[y][x]] = []
            types[g[y][x]].append((x,y))

antinodes = set()
for t in types:
    for i in range(len(types[t])):
        for j in range(i+1, len(types[t])):
            x1, y1 = types[t][i]
            x2, y2 = types[t][j]
            dx, dy = x2-x1, y2-y1
            a1, a2 = (x1-dx, y1-dy), (x2+dx, y2+dy)
            if 0 <= a1[0] < len(lines) and 0 <= a1[1] < len(lines):
                antinodes.add(a1)
            if 0 <= a2[0] < len(lines) and 0 <= a2[1] < len(lines):
                antinodes.add(a2)

print(len(antinodes))

part2 = 0

types = {}

for y in range(h):
    for x in range(w):
        if g[y][x] != ".":
            if g[y][x] not in types:
                types[g[y][x]] = []
            types[g[y][x]].append((x,y))

antinodes = set()

nodes = types.values()
for group in nodes:
    for i in range(len(group)):
        for j in range(len(group)):
            if i == j:
                continue
            x1, y1 = group[i]
            x2, y2 = group[j]
            dx, dy = x2-x1, y2-y1
            x, y = x1, y1
            while 0 <= x < w and 0 <= y < h:
                antinodes.add((x, y))
                x, y = x+dx, y+dy

print(len(antinodes))
