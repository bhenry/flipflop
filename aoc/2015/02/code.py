import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """
"""

sample_answer1 = None
sample_answer2 = None

def process(input):
    return [i.strip().split("x") for i in input.splitlines()]

# print(process(sample_input))

def p1(input):
    data = process(input)
    total = 0
    for d in data:
        l, w, h = int(d[0]), int(d[1]), int(d[2])
        sides = [l*w, w*h, h*l]
        total += 2*sum(sides) + min(sides)

    return total

def p2(input):
    data = process(input)
    total = 0
    for d in data:
        l, w, h = int(d[0]), int(d[1]), int(d[2])
        sides = [l+w, w+h, h+l]
        total += 2*min(sides) + l*w*h
    return total

if p1(input):
    print("\nproblem1", p1(input), "\n\n")

    # debug
    if sample_answer1:
        sample_result = p1(sample_input)
        print("sample1", sample_result)
        if sample_result == sample_answer1:
            print("sample1 test pass")

if p2(input):
    print("\nproblem2", p2(input), "\n\n")

    # debug
    if sample_answer2:
        sample_result = p2(sample_input)
        print("sample2", sample_result)
        if sample_result == sample_answer2:
            print("sample2 test pass")


print("\ndone")
