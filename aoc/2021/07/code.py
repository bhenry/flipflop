from collections import Counter
import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """16,1,2,0,4,2,7,1,2,14"""

sample_answer1 = 37
sample_answer2 = 168

def process(input):
    return [int(i) for i in input.strip().split(",")]

# print(process(sample_input))

def p1(input):
    data = Counter(process(input))
    options = [0] * (max(data.keys()) + 1)
    for i in range(len(options)):
        for pos, count in data.items():
            fuel = abs(int(pos) - i)
            options[i] += fuel * count
    return min(options)

def p2(input):
    data = Counter(process(input))
    options = [0] * (max(data.keys()) + 1)
    for i in range(len(options)):
        for pos, count in data.items():
            fuel = abs(int(pos) - i)
            options[i] += (fuel*(fuel + 1)/2) * count
    return int(min(options))

if sample_answer1:
    sample_result = p1(sample_input)
    print("sample1 test", sample_result == sample_answer1)
    print("sample1", p1(sample_input))
    print("Problem1", p1(input), "\n\n")
if sample_answer2:
    sample_result = p2(sample_input)
    print("sample2 test", sample_result == sample_answer2)
    print("sample2", p2(sample_input))
    print("Problem2", p2(input))
