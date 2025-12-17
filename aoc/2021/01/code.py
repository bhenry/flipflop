import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """199
200
208
210
200
207
240
269
260
263
"""

sample_answer1 = 7
sample_answer2 = 5

def process(input):
    input = [int(i.strip()) for i in input.splitlines() if i.strip()]
    return input

def p1(input):
    data = process(input)
    incs = 0
    last = None
    for d in data:
        if last and d > last:
            incs += 1
        last = d
    return incs

def p2(input):
    data = process(input)
    incs = 0
    last3 = data[:3]
    for d in data[3:]:
        s = sum(last3)
        last3 = last3[1:] + [d]
        sd = sum(last3)
        if sd > s:
            incs += 1
    return incs


if sample_answer1:
    print("sample test", p1(sample_input) == sample_answer1)
    print("Problem1", p1(input))
if sample_answer2:
    print("sample test2", p2(sample_input) == sample_answer2)
    print("Problem2", p2(input))
