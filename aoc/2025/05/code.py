import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import nums, rawfile
path_to_day = os.path.dirname(__file__)
raw = rawfile(f'{path_to_day}/input.txt')

# lines = raw.split("\n")

sample = """3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""
# lines = sample.strip().split("\n")
ranges, ingredients = raw.split("\n\n")
# ranges, ingredients = sample.split("\n\n")

part1 = 0

for ingredient in ingredients.split("\n"):
    for r in ranges.split("\n"):
        a,b = r.split("-")
        if int(ingredient) >= int(a) and int(ingredient) <= int(b):
            part1 += 1
            break

print(part1)

part2 = 0

processed = []

rs = ranges.split("\n")

while rs:
    a,b = rs[0].split("-")
    a = int(a)
    b = int(b)
    rs = rs[1:]
    skip = False
    for p in processed:
        if a >= p[0] and a <= p[1]:
            a = p[1] + 1
        if b >= p[0] and b <= p[1]:
            b = p[0] - 1
        if a <= p[0] and b >= p[1]:
            rs.append(f"{a}-{p[0]-1}")
            rs.append(f"{p[1]+1}-{b}")
            skip = True
    if a <= b and not skip:
        processed.append((int(a), int(b)))

for p in processed:
    part2 += p[1] - p[0] + 1

print(part2)
