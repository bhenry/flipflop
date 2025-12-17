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


pzz = puzzleinput.input

def lookandsay(pz):
    c = 1
    latest = pz[0]
    new = ''
    for d in pz[1:]:
        if latest == d:
            c += 1
        else:
            new = new + str(c) + latest
            c = 1
        latest = d
    return new + str(c) + latest

"""
3113322113
132123222113
111312111213322113

"""

def problem1(pz):
    results = [pz]
    for i in range(40):
        pz = lookandsay(pz)
        results.append(pz)
    return len(pz)

def problem2(pz):
    results = [pz]
    for i in range(50):
        pz = lookandsay(pz)
        results.append(pz)
    return len(pz)

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
