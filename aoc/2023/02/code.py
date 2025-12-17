import os
import re
import sys
APP_DIR = os.path.abspath(__file__).split("adventofcode")[0]+"adventofcode"
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

samples = {
"""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""": 8
}
sample2s = {
"""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""": 2286
}

def process(pz):
    return pz.lines()
pzz = process(puzzleinput)

def problem1(pz):
    running = 0
    for g in pz:
        totals = {"impossible": False, "green": 0, "blue": 0, "red": 0}
        id, game = g.split(":")
        id = int(id.split(" ")[1])
        for session in game.split(";"):
            for turn in session.split(","):
                v = int(re.findall(r"\d+", turn)[0])
                if "green" in turn:
                    totals["green"] += v
                elif "blue" in turn:
                    totals["blue"] += v
                elif "red" in turn:
                    totals["red"] += v
                if totals["green"] > 13:
                    totals["impossible"] = True
                    break
                if totals["blue"] > 14:
                    totals["impossible"] = True
                    break
                if totals["red"] > 12:
                    totals["impossible"] = True
                    break
            if totals["impossible"]:
                break
            else:
                totals["green"] = 0
                totals["blue"] = 0
                totals["red"] = 0
        if not totals.get("impossible"):
            running += id

    return running

def problem2(pz):
    running = 0
    for g in pz:
        totals = {"impossible": False, "green": 0, "blue": 0, "red": 0}
        id, game = g.split(":")
        id = int(id.split(" ")[1])
        for session in game.split(";"):
            for turn in session.split(","):
                v = int(re.findall(r"\d+", turn)[0])
                if "green" in turn:
                    totals["green"] = max(totals["green"], v)
                elif "blue" in turn:
                    totals["blue"] = max(totals["blue"], v)
                elif "red" in turn:
                    totals["red"] = max(totals["red"], v)
        running += totals["green"] * totals["blue"] * totals["red"]

    return running

    return None

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
