import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

sample_answer1 = 2
sample_answer2 = 4

def process(input):
    return [i.strip() for i in input.splitlines()]

print(process(sample_input))

def p1(input):
    data = process(input)
    bad = 0
    for line in data:
        a,b = line.split(",")
        r1,r2 = a.split("-")
        r3,r4 = b.split("-")
        one_in_two = int(r3) <= int(r1) <= int(r4) and int(r3) <= int(r2) <= int(r4)
        two_in_one = int(r1) <= int(r3) <= int(r2) and int(r1) <= int(r4) <= int(r2)
        if one_in_two or two_in_one:
            bad += 1
    return bad

def p2(input):
    data = process(input)
    bad = 0
    for line in data:
        a,b = line.split(",")
        r1,r2 = a.split("-")
        r3,r4 = b.split("-")
        s1 = set(range(int(r1),int(r2)+1))
        s2 = set(range(int(r3),int(r4)+1))
        if s1 & s2:
            bad += 1
    return bad

if sample_answer1:
    print("sample test", p1(sample_input) == sample_answer1)
    print("Problem1", p1(input))
if sample_answer2:
    print("sample test2", p2(sample_input) == sample_answer2)
    print("Problem2", p2(input))
