import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """
"""

sample_answer1 = None
sample_answer2 = None

def process(input):
    return [i.strip() for i in input.splitlines()][0]

# print(process(sample_input))

def p1(input):
    data = process(input)
    cur = [0,0]
    houses = {tuple(cur): 1}
    for h in data:
        cur = list(cur)
        if h == '^':
            cur[1] += 1
        elif h == 'v':
            cur[1] -= 1
        elif h == '>':
            cur[0] += 1
        elif h == '<':
            cur[0] -= 1
        cur = tuple(cur)
        if cur not in houses:
            houses[cur] = 0
        houses[cur] += 1


    return len(houses)

def p2(input):
    data = process(input)
    cur = [[0,0],[0,0]]
    houses = {tuple(cur[0]): 1}
    for i, h in enumerate(data):
        cur[i%2] = list(cur[i%2])
        if h == '^':
            cur[i%2][1] += 1
        elif h == 'v':
            cur[i%2][1] -= 1
        elif h == '>':
            cur[i%2][0] += 1
        elif h == '<':
            cur[i%2][0] -= 1
        cur[i%2] = tuple(cur[i%2])
        if cur[i%2] not in houses:
            houses[cur[i%2]] = 0
        houses[cur[i%2]] += 1
    return len(houses)

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
