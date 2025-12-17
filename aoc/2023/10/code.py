import os
import sys
APP_DIR = os.path.abspath(__file__).split("adventofcode")[0]+"adventofcode"
sys.path.append(APP_DIR)
from lib.util import Input, Grid
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

samples = {
"""..F7.
.FJ|.
SJ.L7
|F--J
LJ...""": 8,
""".....
.S-7.
.|.|.
.L-J.
.....""": 4,
}
sample2s = {

}

def process(pz):
    return pz

def north(pos):
    x, y = pos
    return (x, y-1)

def south(pos):
    x, y = pos
    return (x, y+1)

def east(pos):
    x, y = pos
    return (x+1, y)

def west(pos):
    x, y = pos
    return (x-1, y)


def startconnections(grid, pos):
    x, y = pos
    spot = grid.get(x, y)
    conns = []
    for n, v in grid.neighborsmap(x, y).items():
        if v == ".":
            continue
        if v == "J":
            if n == south(pos) or n == east(pos):
                conns.append(n)
            continue
        if v == "L":
            if n == south(pos) or n == west(pos):
                conns.append(n)
            continue
        if v == "F":
            if n == north(pos) or n == west(pos):
                conns.append(n)
            continue
        if v == "|":
            if n == north(pos) or n == south(pos):
                conns.append(n)
            continue
        if v == "-":
            if n == east(pos) or n == west(pos):
                conns.append(n)
            continue
        if v == "7":
            if n == east(pos) or n == north(pos):
                conns.append(n)
            continue
    return conns

def connections(grid, pos):
    x, y = pos
    spot = grid.get(x, y)
    conns = []
    for n, v in grid.neighborsmap(x, y).items():
        if v == ".":
            continue
        if v == "S":
            continue
        if v == "J":
            if (
                (n == south(pos) and spot in ["7", "F", "|"]) or
                (n == east(pos) and spot in ["F", "L", "-"])
            ):
                conns.append(n)
            continue
        if v == "L":
            if (
                (n == south(pos) and spot in ["7", "F", "|"]) or
                (n == west(pos) and spot in ["7", "J", "-"])
            ):
                conns.append(n)
            continue
        if v == "F":
            if (
                (n == north(pos) and spot in ["L", "J", "|"]) or
                (n == west(pos) and spot in ["J", "7", "-"])
            ):
                conns.append(n)
            continue
        if v == "|":
            if (
                (n == north(pos) and spot in ["L", "J", "|"]) or
                (n == south(pos) and spot in ["7", "F", "|"])
            ):
                conns.append(n)
            continue
        if v == "-":
            if (
                (n == east(pos) and spot in ["F", "L", "-"]) or
                (n == west(pos) and spot in ["J", "7", "-"])
            ):
                conns.append(n)
            continue
        if v == "7":
            if (
                (n == east(pos) and spot in ["F", "L", "-"]) or
                (n == north(pos) and spot in ["L", "J", "|"])
            ):
                conns.append(n)
            continue
    return conns

def problem1(pz):
    grid = pz.grid()

    for pos, val in grid.grid.items():
        if val == "S":
            start = pos
            break

    path1 = []
    path2 = []
    conns = startconnections(grid, start)
    path1.append(conns[0])
    path2.append(conns[1])
    while True:
        if path1[-1] in path2:
            break
        for c in connections(grid, path1[-1]):
            if c not in path1:
                path1.append(c)
        for c in connections(grid, path2[-1]):
            if c not in path2:
                path2.append(c)
    return len(path1)

def problem2(pz):
    grid = pz.grid()

    for pos, val in grid.grid.items():
        if val == "S":
            start = pos
            break

    path1 = []
    path2 = []
    conns = startconnections(grid, start)
    path1.append(conns[0])
    path2.append(conns[1])
    while True:
        if path1[-1] in path2:
            break
        for c in connections(grid, path1[-1]):
            if c not in path1:
                path1.append(c)
        for c in connections(grid, path2[-1]):
            if c not in path2:
                path2.append(c)
    tunnel = set(path1 + path2 + [start])



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
