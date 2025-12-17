from collections import Counter, defaultdict
import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """3,4,3,1,2
"""

sample_answer1 = 5934
sample_answer2 = 26984457539

def process(input):
    return [i.strip() for i in input.splitlines()]

def p1(input):
    data = process(input)[0]
    fishes = [int(i) for i in data.split(",")]

    for _ in range(80):
        fishes = [f - 1 for f in fishes]
        fishes = fishes + [6 for f in fishes if f < 0] + [8 for f in fishes if f < 0]
        fishes = [f for f in fishes if f >= 0]
    return len(fishes)

def p2(input):
    data = process(input)[0]
    fishes = Counter([int(i) for i in data.split(",")])
    for d in range(256):
        new_fishes = defaultdict(int)
        for f, c in fishes.items():
            if f == 0:
                new_fishes[6] += c
                new_fishes[8] += c
            else:
                new_fishes[f - 1] += c
        fishes = new_fishes
    return sum(fishes.values())

if sample_answer1:
    print("sample test", p1(sample_input) == sample_answer1)
    print("Sample1", p1(sample_input))
    print("Problem1", p1(input), "\n\n")
if sample_answer2:
    ans2 = p2(sample_input)
    print("sample test2", ans2 == sample_answer2)
    print("Sample2", ans2)
    print("Problem2", p2(input))
