import os
import sys
APP_DIR = os.path.abspath(__file__).split("adventofcode")[0]+"adventofcode"
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

samples = {
"""seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""":35
}
sample2s = {
"""seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""":46
}

def process(pz):
    return pz
pzz = process(puzzleinput)

def problem1(pz):
    seeds = [int(s) for s in pz.lines()[0].split(": ")[1].split(" ")]
    maps = pz.input.split("\n\n")[1:]
    store = {s:s for s in seeds}
    for m in maps:
        converts = set()
        for line in m.split("\n")[1:]:
            for seed in store:
                dest, source, length = [int(s) for s in line.split(" ")]
                if store[seed] in range(source, source+length) and seed not in converts:
                    store[seed] = dest + (store[seed] - source)
                    converts.add(seed)
                else:
                    store[seed] = store[seed]

    return min(store.values())

def problem2(pz):
    seeds, *rest = pz.input.split("\n\n")
    seed_ranges = [int(s) for s in seeds.split(": ")[1].split()]
    collect = []

    for i in range(0, len(seed_ranges), 2):
        collect.append((seed_ranges[i], seed_ranges[i] + seed_ranges[i + 1]))

    for mapping in rest:
        conversions = []
        for line in mapping.split("\n")[1:]:
            conversions.append([int(s) for s in line.split(" ")])
        new = []
        while len(collect) > 0:
            a, b = collect.pop()
            for dest, src, lng in conversions:
                low = max(a, src)
                high = min(b, src + lng)
                if low < high: # conversion ranges intersect
                    new.append((low - src + dest, high - src + dest))
                    if low > a:
                        collect.append((a, low))
                    if b > high:
                        collect.append((high, b))
                    break
            else:
                new.append((a, b))
        collect = new

    return min(collect)[0]

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
