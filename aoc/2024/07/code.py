import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

lines = puzzleinput.lines()

sample = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
# lines = sample.strip().split("\n")

part1 = 0

for line in lines:
    a = int(line.split(":")[0])
    b = line.split(":")[1].strip()
    c = [int(q) for q in b.split(" ")]
    track = set([c.pop(0)])
    for n in c:
        new_track = set()
        for t in list(track):
            if t + n <= a:
                new_track.add(t + n)
            if t * n <= a:
                new_track.add(t * n)
        track = new_track
    if a in track:
        part1 += a

print(part1)

part2 = 0

for line in lines:
    a = int(line.split(":")[0])
    b = line.split(":")[1].strip()
    c = [int(q) for q in b.split(" ")]
    track = set([c.pop(0)])
    for n in c:
        new_track = set()
        for t in list(track):
            if t + n <= a:
                new_track.add(t + n)
            if t * n <= a:
                new_track.add(t * n)
            if int(str(t) + str(n)) <= a:
                new_track.add(int(str(t) + str(n)))
        track = new_track
    if a in track:
        part2 += a

print(part2)
