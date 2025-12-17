import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import nums, rawfile
path_to_day = os.path.dirname(__file__)
raw = rawfile(f'{path_to_day}/input.txt')

lines = raw.split("\n")

sample = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""
# lines = sample.strip().split("\n")

part1 = 0

pointer = 50
for line in lines:
    if line:
        dir = line[0]
        dist = int(line[1:])
        if dir == 'L':
            pointer = (pointer - dist) % 100
        elif dir == 'R':
            pointer = (pointer + dist) % 100
        if pointer == 0:
            part1 += 1

print(part1)

part2 = 0
pointer = 50

for line in lines:
    if line:
        dir = line[0]
        dist = int(line[1:])

        if dir == 'L':
            if pointer == 0:
                part2 -= 1
            if pointer - dist <= 0:
                part2 += -1*(pointer - dist)//100 + 1
            pointer = (pointer - dist) % 100
        elif dir == 'R':
            if pointer + dist >= 100:
                part2 += (pointer + dist)//100
            pointer = (pointer + dist) % 100


print(part2)
