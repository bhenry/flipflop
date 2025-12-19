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
pos = 0,0
steps = 0
for line in lines:
    x,y = nums(line)
    steps = steps + abs(x-pos[0]) + abs(y - pos[1])
    pos = x,y
print(steps)

part2 = 0
pos = 0,0
steps = 0
for line in lines:
    x,y = nums(line)
    dx = abs(x - pos[0])
    dy = abs(y - pos[1])
    extra = abs(dx-dy)
    steps = steps + min(dx,dy) + extra
    pos = x,y
print(steps)

part3 = 0
neworder = []
for line in lines:
    x,y = nums(line)
    neworder.append((x+y, x, y))
neworder = sorted(neworder)
pos = 0,0
steps = 0
for _,x,y in neworder:
    dx = abs(x - pos[0])
    dy = abs(y - pos[1])
    extra = abs(dx-dy)
    steps = steps + min(dx,dy) + extra
    pos = x,y
print(steps)
