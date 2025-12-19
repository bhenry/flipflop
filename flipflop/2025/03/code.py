import os
import sys
APP_DIR = os.path.abspath(__file__).split("flipflop")[0]
sys.path.append(APP_DIR)
from lib.util import nums, rawfile
path_to_day = os.path.dirname(__file__)
raw = rawfile(f'{path_to_day}/input.txt')

lines = raw.split("\n")

sample = """
"""
# lines = sample.strip().split("\n")

part1 = 0
colors = {}
for line in lines:
    colors[line] = colors.get(line, 0) + 1
part1 = sorted(colors.items(), key=lambda x: x[1], reverse=True)[0][0]
print(part1)
part2 = 0
for line in lines:
    r,g,b = line.split(",")
    if r == g or g == b or r == b:
        continue
    if g > r and g > b:
        part2 += 1
print(part2)


part3 = 0
for line in lines:
    r,g,b = line.split(",")
    if r == g or g == b or r == b:
        part3 += 10
    elif g > r and g > b:
        part3 += 2
    elif r > g and r > b:
        part3 += 5
    elif b > r and b > g:
        part3 += 4
    else:
        assert False
print(part3)
