import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import nums, rawfile
path_to_day = os.path.dirname(__file__)
raw = rawfile(f'{path_to_day}/input.txt')

lines = raw.split("\n")

sample = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""
# lines = sample.strip().split("\n")

part1 = 0

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "@":
            neighbors = []
            for y2 in range(y-1, y+2):
                for x2 in range(x-1, x+2):
                    if x2 == x and y2 == y: continue
                    if 0 <= y2 < len(lines) and 0 <= x2 < len(line):
                        if lines[y2][x2] == "@":
                            neighbors.append(lines[y2][x2])
            if len(neighbors) < 4:
                part1 += 1
print(part1)
part2 = 0

while True:
    updated = False
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "@":
                neighbors = []
                for y2 in range(y-1, y+2):
                    for x2 in range(x-1, x+2):
                        if x2 == x and y2 == y: continue
                        if 0 <= y2 < len(lines) and 0 <= x2 < len(line):
                            if lines[y2][x2] == "@":
                                neighbors.append(lines[y2][x2])
                if len(neighbors) < 4:
                    lines[y] = lines[y][:x] + "." + lines[y][x+1:]
                    updated = True
                    part2 += 1
    if not updated:
        break
print(part2)
