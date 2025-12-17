import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

line = puzzleinput.lines()[0]

sample = "2333133121414131402"
# line = sample

part1 = 0

fs = []
if len(line) % 2 == 0:
    fs = zip([int(x) for x in line[::2]], [int(x) for x in line[1::2]])
else:
    line += '0'
    fs = zip([int(x) for x in line[::2]], [int(x) for x in line[1::2]])

mapp = []
for i, f in enumerate(list(fs)):
    for j in range(f[0]):
        mapp.append(i)
    for j in range(f[1]):
        mapp.append('.')

newmap = []

while "." in mapp:
    left = mapp.index('.')
    right = len(mapp) - 1
    mapp[left], mapp[right] = mapp[right], mapp[left]
    while mapp[-1] == '.':
        mapp.pop()

for i, n in enumerate(mapp):
    part1 += int(n) * (i)

print(part1)

part2 = 0

fs = []
if len(line) % 2 == 0:
    fs = zip([int(x) for x in line[::2]], [int(x) for x in line[1::2]])
else:
    line += '0'
    fs = zip([int(x) for x in line[::2]], [int(x) for x in line[1::2]])

mapp = []
for i, f in enumerate(list(fs)):
    for j in range(f[0]):
        mapp.append(i)
    for j in range(f[1]):
        mapp.append('.')

newmap = [[mapp.pop(0)]]

for thing in mapp:
    latest = newmap[-1][-1]
    if thing == latest:
        newmap[-1].append(thing)
    else:
        newmap.append([thing])

ttm = len(newmap) - 1
while ttm > 0:
    if newmap[ttm][0] == ".":
        ttm -= 1
        continue

    thing_to_move = newmap[ttm]
    for i in range(len(newmap)):
        block = newmap[i]
        if i >= ttm: break
        if block[0] != ".": continue
        blocksize, thingsize = len(block), len(thing_to_move)
        if blocksize < thingsize: continue
        newmap[ttm] = ["." for n in range(thingsize)]
        if leftover := ["." for n in range(blocksize - thingsize)]:
            newmap[i] = leftover
            newmap.insert(i, thing_to_move)
            ttm += 1
        else:
            newmap[i] = thing_to_move
        break
    ttm -= 1

flat = [x for xs in newmap for x in xs]
for i, n in enumerate(flat):
    if n == ".": continue
    part2 += int(n) * (i)

print(part2)
