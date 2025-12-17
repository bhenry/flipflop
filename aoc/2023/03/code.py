import os
import re
import sys
APP_DIR = os.path.abspath(__file__).split("adventofcode")[0]+"adventofcode"
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

samples = {
"""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""": 4361
}
sample2s = {
"""
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".strip(): 467835
}

def process(pz):
    return pz
pzz = process(puzzleinput)

def checker(point):
    return point != "." and not point.isdigit()

def problem1(pz):
    grid = pz.grid()
    collect = []
    for i, line in enumerate(pz.lines()):
        nums = re.findall(r'\d+', line)
        for num in nums:
            ix = line.index(num)
            length = len(num)
            check = range(max(0,ix-1), min(len(line),ix+length+1))
            for x in check:
                prevlinepoint = grid.point(x, max(i-1, 0))
                point = grid.point(x, i)
                nextlinepoint = grid.point(x, min(i+1, grid.h-1))
                if checker(prevlinepoint) or checker(point) or checker(nextlinepoint):
                    collect.append(int(num))
                    collected = True
            line = line.replace(num, "0"*length, 1)

    return sum(collect)

def collectNum(grid, x, y):
    point = grid.point(x, y)
    if point.isdigit():
        digits = [point]
        # look left until no more digits
        for x2 in range(x-1, -1, -1):
            point = grid.point(x2, y)
            if point.isdigit():
                digits.insert(0, point)
            else:
                break
        # look right until no more digits
        for x2 in range(x+1, grid.w):
            point = grid.point(x2, y)
            if point.isdigit():
                digits.append(point)
            else:
                break
        return int("".join(digits))
    return 0

def getratio(grid, x, y):
    neighbors = grid.neighbors(x, y)
    top = neighbors[0:3]
    left = neighbors[3]
    right = neighbors[4]
    bottom = neighbors[5:8]
    store = []
    if left.isdigit():
        store.append(collectNum(grid, x-1, y))
    if right.isdigit():
        store.append(collectNum(grid, x+1, y))
    if all([i.isdigit() for i in top]):
        store.append(collectNum(grid, x, y-1))
    else:
        if top[0].isdigit():
            store.append(collectNum(grid, x-1, y-1))
        if top[2].isdigit():
            store.append(collectNum(grid, x+1, y-1))
        if top[1].isdigit() and not (top[0].isdigit() or top[2].isdigit()):
            store.append(collectNum(grid, x, y-1))
    if all([i.isdigit() for i in bottom]):
        store.append(collectNum(grid, x, y+1))
    else:
        if bottom[0].isdigit():
            store.append(collectNum(grid, x-1, y+1))
        if bottom[2].isdigit():
            store.append(collectNum(grid, x+1, y+1))
        if bottom[1].isdigit() and not (bottom[0].isdigit() or bottom[2].isdigit()):
            store.append(collectNum(grid, x, y+1))
    if len(store) == 2:
        return store[0] * store[1]
    return 0

def problem2(pz):
    grid = pz.grid()
    collect = []
    total = 0
    for i, line in enumerate(pz.lines()):
        for j, point in enumerate(line):
            if point == "*":
                total += getratio(grid, j, i)
    return total

# debug
if sample2s:
    for sample in sample2s:
        sample_result = problem2(process(Input(sample)))
        print("sample2", sample_result)
        if sample_result == sample2s[sample]:
            print("sample2 test pass")

if answer2 := problem2(pzz):
    print("\nproblem2", answer2, "\n\n")

# debug
if samples:
    for sample in samples:
        sample_result = problem1(process(Input(sample)))
        print("sample1", sample_result)
        if sample_result == samples[sample]:
            print("sample1 test pass")

if answer1 := problem1(pzz):
    print("\nproblem1", answer1, "\n\n")


print("\ndone")
