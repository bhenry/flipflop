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
    return pz.input.split("\n\n")

def problem1(pz):
    rules, wfs = process(pz)
    rmap = {}
    for rule in rules.splitlines():
        rule_name, rule = rule.split("{")
        rule = rule.strip("}")
        rmap[rule_name] = rule.split(",")
    totes = 0
    for wf in wfs.splitlines():
        hmap = eval(wf.replace("x=", "'x':").replace("m=", "'m':").replace("a=", "'a':").replace("s=", "'s':"))
        x, m, a, s = hmap["x"], hmap["m"], hmap["a"], hmap["s"]
        start = "in"
        while True:
            for r in rmap[start]:
                if ":" in r:
                    eq, nxt = r.split(":")
                    if eval(eq):
                        start = nxt
                        break
                else:
                    start = r
            if start == "A" or start == "R":
                break
        if start == "A":
            totes += x + m + a + s
    return totes











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
