import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """
"""

sample_answer1 = True
sample_answer2 = True

def process(input):
    return [i.strip() for i in input.splitlines()]

# print(process(sample_input))

def p1(input):
    data = process(input)[0]
    floor = 0
    for c in data:
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
    return floor

def p2(input):
    data = process(input)[0]
    floor = 0
    pos = 1
    for c in data:
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
        if floor == -1:
            return pos
        pos += 1

if sample_answer1:
    # sample_result = p1(sample_input)
    # print("sample1", sample_result)
    # print("sample1 test pass")
    print("\nproblem1", p1(input), "\n\n")

if sample_answer2:
    sample_result = p2(sample_input)
    print("sample2", sample_result)
    if sample_result == sample_answer2:
        print("sample2 test pass")
    print("\nproblem2", p2(input), "\n\n")


print("\ndone")
