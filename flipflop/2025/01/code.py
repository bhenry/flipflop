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
for line in lines:
    ba = line.count("ba")
    na = line.count("na")
    ne = line.count("ne")
    part1 += ba+na+ne
print(part1)
part2 = part1
for line in lines:
    ba = line.count("ba")
    na = line.count("na")
    ne = line.count("ne")
    if (ba + na + ne) % 2 == 1:
        part2 -= ba+na+ne
print(part2)
part3 = part1
for line in lines:
    ba = line.count("ba")
    na = line.count("na")
    ne = line.count("ne")
    if ne > 0:
        part3 -= ba+na+ne
print(part3)
