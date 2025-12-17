import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import nums, rawfile
path_to_day = os.path.dirname(__file__)
raw = rawfile(f'{path_to_day}/input.txt')

lines = raw.split("\n")

sample = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""
# lines = sample.strip().split("\n")
g = [list(l) for l in lines]
w = len(g[0])
h = len(g)
def oob(x,y):
    return x < 0 or x >= w or y < 0 or y >= h

walls = set()
track = set()
for y in range(len(g)):
    for x in range(len(g[y])):
        if g[y][x] == "#":
            walls.add((x, y))
            continue
        if g[y][x] == "S":
            START = (x, y)
        if g[y][x] == "E":
            END = (x, y)
        track.add((x, y))

paths = {}

def get_next(p,f):
    x,y = p
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if (nx, ny) in walls: continue
        if (nx, ny) == f: continue
        return (nx, ny)

startdir = (1, 0) if not sample.strip() else (0, -1)
f = END
# p = get_next((END[0]-1,END[1]),f)
TRACK = [END, (END[0]-1,END[1])]
while True:
    f, p = TRACK[-2:]
    newp = get_next(p,f)
    TRACK.append(newp)
    if newp == START: break

part1 = 0

for wall in walls:
    x,y = wall
    track_neighbors = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if (nx, ny) in walls: continue
        if oob(nx,ny): continue
        track_neighbors.append((nx, ny))
    if len(track_neighbors) > 1:
        for n in track_neighbors:
            for m in track_neighbors:
                if m == n: continue
                a, b = TRACK.index(n), TRACK.index(m)
                if a + 2 > b and a - b - 2 > 0:
                    if (a - b - 2) >= 100:
                        part1 += 1

print(part1)
part2 = 0
