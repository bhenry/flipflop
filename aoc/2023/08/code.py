import os
import sys
from itertools import cycle
from math import lcm
APP_DIR = os.path.abspath(__file__).split("adventofcode")[0]+"adventofcode"
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

samples = {
"""RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
""": 2,
}
sample2s = {
"""LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
""": 6,
}

def process(pz):
    return pz.lines()

def problem1(pz):
    coords = pz.input.split("\n\n")[1].strip().split("\n")
    mapping = {}
    for coord in coords:
        loc, LR = coord.split(" = ")
        L, R = LR.split(", ")
        L = L[1:]
        R = R[:-1]
        mapping[loc] = (L, R)
    last = "AAA"
    steps = 0
    for inst in cycle(pz.lines()[0]):
        if inst == "L":
            last = mapping[last][0]
        elif inst == "R":
            last = mapping[last][1]
        else:
            print("WTF")
        if last == "ZZZ":
            break
        steps += 1
    return steps + 1


def problem2(pz):
    coords = pz.input.split("\n\n")[1].strip().split("\n")
    mapping = {}
    start = []
    for coord in coords:
        loc, LR = coord.split(" = ")
        if loc.endswith("A"):
            start.append(loc)
        L, R = LR.split(", ")
        L = L[1:]
        R = R[:-1]
        mapping[loc] = (L, R)
    steps = 1
    last = start
    cache = {}
    for inst in cycle(pz.lines()[0]):
        new_last = []
        for loc in last:
            n = mapping[loc][0 if inst == "L" else 1]
            new_last.append(n)
            if n.endswith("Z"):
                cache[loc] = steps
        steps += 1
        last = new_last
        if len(cache) == len(start):
            return lcm(*cache.values())

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
