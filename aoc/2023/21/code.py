import os
import sys
APP_DIR = os.path.abspath(__file__).split("adventofcode")[0]+"adventofcode"
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

samples = {
# """...........
# .....###.#.
# .###.##..#.
# ..#.#...#..
# ....#.#....
# .##..S####.
# .##..#...#.
# .......##..
# .##.#.####.
# .##..##.##.
# ...........""": 16
}
sample2s = {

}

def process(pz):
    return pz.grid()

def problem1(pz):
    pz = process(pz)
    g = pz.grid
    start = [k for k,v in g.items() if v == "S"][0]
    places = [start]
    for move in range(64):
        newplaces = set()
        for place in places:
            ns = pz.neighborsmap(*place, diag=False)
            for n in ns:
                if n not in g:
                    continue
                if g[n] == "#":
                    continue
                if g[n] in ".S":
                    newplaces.add(n)
        places = newplaces
    return len(places)

def problem2(pz):
    pz = process(pz)
    g = pz.grid
    start = [k for k,v in g.items() if v == "S"][0]
    places = [start]
    for move in range(26501365):
        newplaces = set()
        for place in places:
            placeirl = (place[0]%pz.w, place[1]%pz.h)
            ns = pz.neighborslocs(*place, diag=False)
            for n in ns:
                nirl = (n[0]%pz.w,n[1]%pz.h)
                if nirl not in g:
                    continue
                if g[nirl] == "#":
                    continue
                if g[nirl] in ".S":
                    newplaces.add(n)
        places = newplaces
    return len(places)

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
