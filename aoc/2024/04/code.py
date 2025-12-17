import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

lines = puzzleinput.lines()

part1 = 0

sample = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

# lines = sample.strip().split("\n")

cols = ["".join([line[i] for line in lines]) for i in range(len(lines[0]))]

def xmas(s):
    return s.count("XMAS") + s.count("SAMX")

def get_diags(lines):
    diags = []
    for i in range(len(lines)):
        diag = ""
        for j in range(len(lines)-i):
            diag += lines[j][j+i]
        diags.append(diag)
    return diags

def p (lines):
    for line in lines:
        print(line)
    print()
# p(lines)
# p([line[::-1] for line in cols])
# p([line[::-1] for line in lines[::-1]])
# p(cols[::-1])

diags = get_diags(lines)
diags += get_diags([line[::-1] for line in cols])
diags += get_diags([line[::-1] for line in lines[::-1]])[1:]
diags += get_diags(cols[::-1])[1:]

for line in lines:
    part1 += xmas(line)

for col in cols:
    part1 += xmas(col)

for diag in diags:
    part1 += xmas(diag)

print(part1)


part2 = 0

def _tl(lines,y,x):
    return lines[y-1][x-1]
def _tr(lines,y,x):
    return lines[y+1][x-1]
def _bl(lines,y,x):
    return lines[y-1][x+1]
def _br(lines,y,x):
    return lines[y+1][x+1]

for x in range(1,len(lines)-1):
    for y in range(1,len(lines)-1):
        if lines[y][x] == "A":
            tl, br = _tl(lines,y,x), _br(lines,y,x)
            tr, bl = _tr(lines,y,x), _bl(lines,y,x)
            if {tl,br} == {"M","S"} and {tr,bl} == {"M","S"}:
                part2 += 1

print(part2)
