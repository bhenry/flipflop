import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

sample_answer1 = "CMZ"
sample_answer2 = "MCD"

def process(input):
    return [i for i in input.splitlines()]

def move_one(stacks, frm, to):
    stacks[(to) - 1] = [stacks[(frm) - 1][0]] + stacks[(to) - 1]
    stacks[(frm) - 1] = stacks[(frm) - 1][1:]

def p1(input):
    data = process(input)
    rows = []
    for line in data:
        if line.startswith(" 1   2   3"):
            break
        rows.append([line[i:i + 4] for i in range(0, len(line), 4)])
    stacks = {}
    for row in rows:
        for i in range(len(row)):
            if stacks.get(i):
                stacks[i].append(row[i])
            else:
                stacks[i] = [row[i]]

    for k in stacks:
        stacks[k] = [i.strip() for i in stacks[k] if i.strip()]

    for line in data:
        if line.startswith("move"):
            move = int(line.split(" ")[1])
            frm = int(line.split(" ")[3])
            to = int(line.split(" ")[5])
            for i in range(move):
                move_one(stacks, frm, to)
    answer = ""
    for k in stacks:
        answer += stacks[k][0]
    return ''.join(x for x in answer if x.isalpha())

def move_all(stacks, frm, to, move):
    stacks[(to) - 1] = stacks[(frm) - 1][0:move] + stacks[(to) - 1]
    stacks[(frm) - 1] = stacks[(frm) - 1][move:]

def p2(input):
    data = process(input)
    rows = []
    for line in data:
        if line == " 1   2   3":
            break
        rows.append([line[i:i + 4] for i in range(0, len(line), 4)])
    stacks = {}
    for row in rows:
        for i, stack in enumerate(row):
            if stacks.get(i):
                stacks[i].append(row[i])
            else:
                stacks[i] = [row[i]]

    for k in stacks:
        stacks[k] = [i.strip() for i in stacks[k] if i.strip()]

    for line in data:
        if line.startswith("move"):
            move = int(line.split(" ")[1])
            frm = int(line.split(" ")[3])
            to = int(line.split(" ")[5])
            move_all(stacks, frm, to, move)
    answer = ""
    for k in stacks:
        answer += stacks[k][0]
    return ''.join(x for x in answer if x.isalpha())

if sample_answer1:
    print("sample test", p1(sample_input) == sample_answer1)
    print("Problem1", p1(input))
if sample_answer2:
    print("sample test2", p2(sample_input) == sample_answer2)
    print("Problem2", p2(input))
