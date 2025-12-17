import os
import sys
APP_DIR = os.path.abspath(__file__).split("adventofcode")[0]+"adventofcode"
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

samples = {
"""0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""":114
}
sample2s = {
list(samples.keys())[0]: 2
}

def process(pz):
    return pz.lines()

def getdiffs(numbers):
    diffs = []
    for i in range(1, len(numbers)):
        diffs.append(numbers[i] - numbers[i-1])
    return diffs

def climbup(difftree):
    return sum([d[-1] for d in difftree])


def problem1(pz):
    lines = process(pz)
    new_nums = []
    for line in lines:
        numbers = [int(n) for n in line.split()]
        difftree = [numbers]
        while difftree[-1] != [0]*len(difftree[-1]):
            difftree.append(getdiffs(difftree[-1]))
        new_nums.append(climbup(difftree))
    return sum(new_nums)

def climbup2(difftree):
    for i in range(1, len(difftree)):
        new = difftree[-i-1][0] - difftree[-i][0]
        difftree[-i-1][0] = new
    return difftree[0][0]

def problem2(pz):
    lines = process(pz)
    new_nums = []
    for line in lines:
        numbers = [int(n) for n in line.split()]
        difftree = [numbers]
        while difftree[-1] != [0]*len(difftree[-1]):
            difftree.append(getdiffs(difftree[-1]))
        new_nums.append(climbup2(difftree))
    return sum(new_nums)

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
