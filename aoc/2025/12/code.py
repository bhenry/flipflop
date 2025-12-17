import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import nums, rawfile
path_to_day = os.path.dirname(__file__)
raw = rawfile(f'{path_to_day}/input.txt')

stuff = raw.split("\n\n")

sample = """
"""
# lines = sample.strip().split("\n")

part1 = 0

def present_size(p):
    return p.count("#")

def fits(d, presents):
    w,h = [int(x) for x in d.split(":")[0].split("x")]
    space = w*h
    for i, d in enumerate(d.split(":")[1].strip().split()):
        space = space - present_size(presents[i]) * int(d)
    return space >= 0

data = stuff[6]
for d in data.strip().split("\n"):
    if fits(d, stuff[0:6]):
        part1 += 1

print(part1)
part2 = 0
