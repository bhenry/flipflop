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
"""rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7""":145
}

def process(pz):
    return pz.lines()[0].split(",")

def hash(s):
    st = 0
    for c in s:
        st += ord(c)
        st *= 17
        st %= 256
    return st

def problem1(pz):
    strs = process(pz)
    t = 0
    for s in strs:
        t += hash(s)
    return t

def problem2(pz):
    strs = process(pz)
    hm = {}
    for s in strs:
        if "=" in s:
            lens, f = s.split("=")
            k = hash(lens)
            if k in hm and hm[k]:
                hm[k][lens] = int(f)
            else:
                hm[k] = {lens: int(f)}
        else:
            lens = s.split("-")[0]
            k = hash(lens)
            if k in hm:
                hm[k].pop(lens, None)

    t = 0
    for box in hm:
        for lens in hm[box]:
            t += (box+1)*hm[box][lens]*(list(hm[box].keys()).index(lens)+1)
    return t

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
