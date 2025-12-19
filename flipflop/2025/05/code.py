import os
import sys
APP_DIR = os.path.abspath(__file__).split("flipflop")[0]
sys.path.append(APP_DIR)
from lib.util import nums, rawfile
path_to_day = os.path.dirname(__file__)
raw = rawfile(f'{path_to_day}/input.txt')

line = raw.strip()

sample = """
"""
# lines = sample.strip().split("\n")

part1 = 0
pos = 0
c = line[pos]
while True:
    if line.index(c) < pos:
        part1 += pos - line.index(c)
        pos = line.index(c) + 1
    else:
        part1 += line.index(c, pos+1) - pos
        pos = line.index(c, pos+1) + 1
    if pos >= len(line):
        break
    c = line[pos]
print(part1)

pos = 0
c = line[pos]
visited = set()
while True:
    if line.index(c) < pos:
        pos = line.index(c) + 1
    else:
        pos = line.index(c, pos+1) + 1
    if pos >= len(line):
        break
    c = line[pos]
    visited.add(c)
unvisited = []
for c in line:
    if c not in visited and c not in unvisited:
        unvisited.append(c)
print(''.join(unvisited))

part3 = 0
pos = 0
c = line[pos]
while True:
    if line.index(c) < pos:
        if c < "a":
            part3 -= pos - line.index(c)
        else:
            part3 += pos - line.index(c)
        pos = line.index(c) + 1
    else:
        if c < "a":
            part3 -= line.index(c, pos+1) - pos
        else:
            part3 += line.index(c, pos+1) - pos
        pos = line.index(c, pos+1) + 1
    if pos >= len(line):
        break
    c = line[pos]
print(part3)
