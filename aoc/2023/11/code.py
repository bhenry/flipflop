import itertools
import os
import sys
APP_DIR = os.path.abspath(__file__).split("adventofcode")[0]+"adventofcode"
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

samples = {
"""...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""": 374
}
"""....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#......."""

sample2s = {
    list(samples.keys())[0]: 1030
}

def process(pz):
    return pz

def problem1(pz):
    new = []
    lines = pz.lines()
    for i in range(len(lines)):
        line = lines[i]
        new.append(line)
        if all([c == "." for c in line]):
            new.append(line)

    new2 = ["" for i in range(len(new))]
    for i in range(len(new)):
        line = new[i]
        for j in range(len(line)):
            new2[i] += line[j]
            if all([new[c][j] == "." for c in range(len(new))]):
                new2[i] += line[j]
    expanded = Input("\n".join(new2)).grid().grid
    store = set()
    for pos, v in expanded.items():
        if v == "#":
            store.add(pos)
    t = 0
    for p1, p2 in set(itertools.combinations(store, 2)):
        t += abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    return t

def problem2(pz):
    g = pz.grid().grid
    t = 0
    store = set()
    w = len(pz.lines()[0])
    h = len(pz.lines())
    for pos, v in g.items():
        if v == "#":
            store.add(pos)
    rows = []
    for i in range(h):
        if all([g[(j, i)] == "." for j in range(w)]):
            rows.append(i)
    cols = []
    for i in range(w):
        if all([g[(i, j)] == "." for j in range(h)]):
            cols.append(i)
    for p1, p2 in set(itertools.combinations(store, 2)):
        t += abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        for i in cols:
            if p1[0] < i < p2[0] or p2[0] < i < p1[0]:
                t += 999999
        for i in rows:
            if p1[1] < i < p2[1] or p2[1] < i < p1[1]:
                t += 999999
    # for p1, p2 in set(itertools.combinations(store, 2)):
    #     t += abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    #     for i in range(p1[0], p2[0]) if p1[0] < p2[0] else range(p2[0], p1[0]):
    #         if check1(g, p1, p2, i, pz):
    #             t += 999999
    #     for i in range(p1[1], p2[1]) if p1[1] < p2[1] else range(p2[1], p1[1]):
    #         if check2(g, p1, p2, i, pz):
    #             t += 999999

    return t

# debug
if sample2s:
    for sample in sample2s:
        sample_result = problem2(Input(sample))
        print("sample2", sample_result)
        if sample_result == sample2s[sample]:
            print("sample2 test pass")

if answer2 := problem2(puzzleinput):
    print("\nproblem2", answer2, "\n\n")

# debug
if samples:
    for sample in samples:
        sample_result = problem1(Input(sample))
        print("sample1", sample_result)
        if sample_result == samples[sample]:
            print("sample1 test pass")

if answer1 := problem1(puzzleinput):
    print("\nproblem1", answer1, "\n\n")


print("\ndone")
