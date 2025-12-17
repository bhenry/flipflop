import os
import sys
APP_DIR = os.path.dirname(os.path.abspath(__file__).split("aoc")[0])
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

samples = {

}
sample2s = {
    """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""": 281

}

def process(pz):
    return pz.lines()

def p1(pz):
    total = 0
    for line in pz:
        a = None
        b = None
        for l in line:
            if l.isnumeric():
                a = l
                break
        for l in line[::-1]:
            if l.isnumeric():
                b = l
                break
        total += int(a + b)
    return total

def p2(pz):
    total = 0
    numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }

    for line in pz:
        locs = {n: line.find(n) for n in numbers.keys() if line.find(n) != -1}
        a = numbers.get(min(locs, key=locs.get))
        locs = {n: line[::-1].find(n[::-1]) for n in numbers.keys() if line.find(n) != -1}
        b = numbers.get(min(locs, key=locs.get))
        print(a, b)
        total += int(str(a) + str(b))
    return total

pzz = process(puzzleinput)

if answer2 := p2(pzz):
    print("\nproblem2", answer2, "\n\n")

# debug
if sample2s:
    for sample in sample2s:
        sample_result = p2(process(Input(sample)))
        print("sample2", sample_result)
        if sample_result == sample2s[sample]:
            print("sample2 test pass")

if answer1 := p1(pzz):
    print("\nproblem1", answer1, "\n\n")

    # debug
    if samples:
        for sample in samples:
            sample_result = p1(Input(sample))
            print("sample1", sample_result)
            if sample_result == samples[sample]:
                print("sample1 test pass")



print("\ndone")
