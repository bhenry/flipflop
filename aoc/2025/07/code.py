import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import nums, rawfile
path_to_day = os.path.dirname(__file__)
raw = rawfile(f'{path_to_day}/input.txt')

lines = raw.split("\n")

sample = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""
# lines = sample.strip().split("\n")

part1 = 0
start = lines[0].find("S")
beams = [start]
for line in lines:
    hit = beams
    for beam in beams:
        if line[beam] == "^":
            part1 += 1
            hit = hit[:hit.index(beam)] + hit[hit.index(beam)+1:]
            if beam-1 not in hit:
                hit.append(beam-1)
            if beam+1 not in hit:
                hit.append(beam+1)
    beams = hit
print(part1)

part2 = 1
start = lines[0].find("S")
beams = {start: 1}

for line in lines:
    for beam in beams.copy():
        if line[beam] == "^":
            ts = beams.pop(beam)
            if beam-1 not in beams:
                beams[beam-1] = ts
            else:
                beams[beam-1] += ts
            if beam+1 not in beams:
                beams[beam+1] = ts
            else:
                beams[beam+1] += ts

print(sum(beams.values()))
