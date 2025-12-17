import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import nums, rawfile
path_to_day = os.path.dirname(__file__)
raw = rawfile(f'{path_to_day}/input.txt')

lines = raw.split("\n\n")

sample = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""
# lines = sample.strip().split("\n\n")

towels = lines[0].strip().split(", ")
patterns = lines[1].strip().split("\n")

part1 = 0
part2 = 0

c = {}
def calc(p):
    if p in c: return c[p]
    if p == "": return 1
    ct = 0
    for t in towels:
        if p.startswith(t):
            newt = p[len(t):]
            ct += calc(newt)
    c[p] = ct
    return ct

for p in patterns:
    numpos = calc(p)
    if numpos:
        part1 += 1
        part2 += numpos

print(part1)
print(part2)
