import os
import sys
APP_DIR = os.path.abspath(__file__).split("adventofcode")[0]+"adventofcode"
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

samples = {

}
sample2s = {

}

def process(pz):
    return pz.lines()
pzz = process(puzzleinput)

def problem1(pz):
    total = 0
    for line in pz:
        ph = len(line)
        ch = len(eval(line))
        total += ph - ch
    return total

def problem2(pz):
    total = 0
    for line in pz:
        ph = len(line)
        ch = len(line.replace('"', '""').replace("\\", "\\\\")) + 2
        total += ch - ph
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
