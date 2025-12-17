import itertools
import os
import sys
APP_DIR = os.path.abspath(__file__).split("adventofcode")[0]+"adventofcode"
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

samples = {
"""London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141""":605
}
sample2s = {
"""London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141""":982
}

def process(pz):
    return pz.lines()
pzz = process(puzzleinput)

def trips_from_puzzle(pz):
    trips = {}
    for line in pz:
        cities, distance = line.split(" = ")
        cities = cities.split(" to ")
        distance = int(distance)
        trips[cities[0]] = trips.get(cities[0], {})
        trips[cities[0]][cities[1]] = distance
        trips[cities[1]] = trips.get(cities[1], {})
        trips[cities[1]][cities[0]] = distance
    return trips

def problem1(pz):
    shortest = None
    trips = trips_from_puzzle(pz)
    shortest = 10000000
    for trip in itertools.permutations(trips.keys()):
        d = 0
        for i in range(len(trip)-1):
            depart = trip[i]
            arrive = trip[i+1]
            d += trips[depart].get(arrive, 10000000)
        if d < shortest:
            shortest = d

    return shortest

def problem2(pz):
    longest = None
    trips = trips_from_puzzle(pz)
    longest = 0
    for trip in itertools.permutations(trips.keys()):
        d = 0
        for i in range(len(trip)-1):
            depart = trip[i]
            arrive = trip[i+1]
            dist = trips[depart].get(arrive)
            if not dist:
                break
            d += dist
        if d > longest:
            longest = d

    return longest

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
