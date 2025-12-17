import os
import sys
APP_DIR = os.path.abspath(__file__).split("adventofcode")[0]+"adventofcode"
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

samples = {
"""O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""":136,
}
"""OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#...."""

sample2s = {

}

def process(pz):
    return pz

def problem1(pz):
    lines = process(pz).lines()
    g = [list(line) for line in lines]
    for _ in range(len(g)):
        for y in range(len(g)-1):
            for x in range(len(g[0])):
                if g[y][x] == "." and g[y+1][x] == "O":
                    g[y][x] = "O"
                    g[y+1][x] = "."
    t = 0
    for l in g:
        t += l.count("O") * (len(g) - g.index(l))
    return t

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

if answer1 := problem1(puzzleinput):
    print("\nproblem1", answer1, "\n\n")


print("\ndone")
