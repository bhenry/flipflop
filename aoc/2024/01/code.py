import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

lines = puzzleinput.lines()
firsts, lasts = [], []
part1 = 0
for i in range(len(lines)):
    a, b = lines[i].split()
    firsts.append(int(a))
    lasts.append(int(b))
firsts = sorted(firsts)
lasts = sorted(lasts)
for i in range(len(lines)):
    a, b = firsts[i], lasts[i]
    part1 += b - a if b > a else a - b

print(part1)
from collections import Counter
frequencies = Counter(lasts)
part2 = 0
for i in range(len(lines)):
    a = firsts[i]
    b = frequencies[a]
    part2 += a * b

print(part2)
