import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import nums, rawfile
path_to_day = os.path.dirname(__file__)
raw = rawfile(f'{path_to_day}/input.txt')

def print_(*args, **kwargs):
    print("\n")
    print(*args, **kwargs)

lines = raw.split("\n")
sort_n = 1000

sample = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""
# lines = sample.strip().split("\n")
# sort_n = 10

part1 = 0
part2 = 0
circuits = []
for i, line in enumerate(lines):
    x, y, z = nums(line)
    circuits.append((x,y,z))

possible_cxs = []
for i in range(len(circuits)):
    for j in range(i+1,len(circuits)):
        c1 = circuits[i]
        c2 = circuits[j]
        dist = sum([(a - b)**2 for (a,b) in zip(c1, c2)])
        possible_cxs.append((c1,c2,dist))

sorted_cxs = sorted(possible_cxs, key=lambda x: x[2])
i = 0
for c1,c2,_dist in sorted_cxs:
    cxs = [circuit for circuit in circuits if c1 == circuit or c2 == circuit or c1 in circuit or c2 in circuit]
    if len(cxs) > 1:
        if isinstance(cxs[0], set) and isinstance(cxs[1], set):
            circuits.append(cxs[0] | cxs[1])
            circuits.remove(cxs[0])
            circuits.remove(cxs[1])
        elif isinstance(cxs[0], set):
            cxs[0].add(c2)
            cxs[0].add(c1)
            if c2 in circuits:
                circuits.remove(c2)
            if c1 in circuits:
                circuits.remove(c1)
        elif isinstance(cxs[1], set):
            cxs[1].add(c1)
            cxs[1].add(c2)
            if c1 in circuits:
                circuits.remove(c1)
            if c2 in circuits:
                circuits.remove(c2)
        else:
            circuits.append({c1, c2})
            circuits.remove(c1)
            circuits.remove(c2)
    elif len(cxs) == 1:
        # both sets are in same circuit
        pass
    else:
        circuits.append({c1, c2})
        circuits.remove(c1)
        circuits.remove(c2)
    if len(circuits) == 1:
        part2 = c1[0]*c2[0]
        if part1 != 0:
            break
    i += 1
    if i == sort_n and part1 == 0:
        circuits = sorted(circuits, key=lambda x: len(x) if isinstance(x, set) else 1)
        part1 = len(circuits[-3]) * len(circuits[-2]) * len(circuits[-1])
        if part2 != 0:
            break

print(part1)
print(part2)
