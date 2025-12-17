import os
import re
import sys
APP_DIR = os.path.abspath(__file__).split("adventofcode")[0]+"adventofcode"
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

samples = {
"""???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""": 21,
}
sample2s = {

}

def process(pz):
    return pz.lines()

def possible(line, cache):
    springs, layout = line.split(" ")
    clusters = [int(x) for x in layout.split(",")]
    springs = [x for x in springs]
    return 0

def problem1(pz):
    lines = process(pz)
    t = 0
    c = {}
    for line in lines:
        q = re.findall(r'([\?#]+)', line)
        t += possible(line, q, c)
        print(q)
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
        print(sample)
        sample_result = problem1(Input(sample))
        print("sample1", sample_result)
        if sample_result == samples[sample]:
            print("sample1 test pass")

# if answer1 := problem1(puzzleinput):
#     print("\nproblem1", answer1, "\n\n")


print("\ndone")
