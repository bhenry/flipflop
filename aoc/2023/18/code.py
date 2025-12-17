import os
import sys
APP_DIR = os.path.abspath(__file__).split("adventofcode")[0]+"adventofcode"
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

samples = {
"""R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)""":62
}
sample2s = {

}

def process(pz):
    return pz.lines()

def problem1(pz):
    lines = process(pz)
    g = {}
    l = (0,0)
    for line in lines:
        dir, dist, _ = line.split()
        dist = int(dist)
        if dir == "R":
            for i in range(dist):
                l = (l[0]+1, l[1])
                g[l] = True
        elif dir == "L":
            for i in range(dist):
                l = (l[0]-1, l[1])
                g[l] = True
        elif dir == "U":
            for i in range(dist):
                l = (l[0], l[1]-1)
                g[l] = True
        elif dir == "D":
            for i in range(dist):
                l = (l[0], l[1]+1)
                g[l] = True

    # find max x and y
    max_x = max_y = 0
    min_x = min_y = 0
    for l in g:
        max_x = max(max_x, l[0])
        max_y = max(max_y, l[1])
        min_x = min(min_x, l[0])
        min_y = min(min_y, l[1])
    # print(max_x, max_y, min_x, min_y)
    c = 0
    for y in range(min_y, max_y+1):
        counting = False
        for x in range(min_x, max_x+1):
            if not counting:
                if (x,y) in g:
                    counting = True
                    c += 1
            else:
                c += 1
                if (x,y) in g:
                    counting = False

def problem2(pz):
    lines = process(pz)

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

# if answer1 := problem1(puzzleinput):
#     print("\nproblem1", answer1, "\n\n")


print("\ndone")
