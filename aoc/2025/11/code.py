import os
import sys
from functools import cache
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import nums, rawfile
path_to_day = os.path.dirname(__file__)
raw = rawfile(f'{path_to_day}/input.txt')

lines = raw.split("\n")

sample = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""
# lines = sample.strip().split("\n")

part1 = 0
paths = {}
for line in lines:
    stuff = line.split(" ")
    paths[stuff[0][:-1]] = stuff[1:]

cxs = paths["you"]
while True:
    new_cxs = []
    for cx in cxs:
        if cx == "out":
            part1 += 1
        else:
            new_cxs.extend(paths[cx])
    cxs = new_cxs
    if not cxs:
        break

print(part1)

sample2 = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty svr
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""
# lines = sample2.strip().split("\n")
part2 = 0
paths = {}
for line in lines:
    stuff = line.split(" ")
    paths[stuff[0][:-1]] = stuff[1:]

@cache
def count_paths(start,end):
    if start == end:
        return 1
    else:
        total = 0
        for cx in paths.get(start, []):
            total += count_paths(cx,end)
    return total

svr_to_fft = count_paths("svr","fft")
fft_to_dac = count_paths("fft","dac")
dac_to_out = count_paths("dac","out")
part2 += svr_to_fft * fft_to_dac * dac_to_out

svr_to_dac = count_paths("svr","dac")
dac_to_fft = count_paths("dac","fft")
fft_to_out = count_paths("fft","out")
part2 += svr_to_dac * dac_to_fft * fft_to_out

print(part2)
