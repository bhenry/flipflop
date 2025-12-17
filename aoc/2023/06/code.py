import os
import sys
APP_DIR = os.path.abspath(__file__).split("adventofcode")[0]+"adventofcode"
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

samples = {
"""Time:      7  15   30
Distance:  9  40  200""": 288
}
sample2s = {

}

def process(pz):
    return pz.lines()
pzz = process(puzzleinput)

def problem1(pz):
    times, distances = pz
    races = {int(a):int(b) for a, b in zip(times.split(": ")[1].split(), distances.split(": ")[1].split())}
    ways_to_win = 1
    for time in races:
        wins = 0
        for t in range(time):
            if t*(time-t) > races[time]:
                wins += 1
        ways_to_win *= wins
    return ways_to_win

def problem2(pz):
    time = 62737565
    d = 644102312401023
    wins = 0
    for t in range(time):
        if t*(time-t) > d:
            wins += 1
    return wins


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
