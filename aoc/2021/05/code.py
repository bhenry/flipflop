import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""

sample_answer1 = 5
sample_answer2 = 12

def process(input):
    data = [i.strip() for i in input.splitlines()]
    return data

def p1(input):
    data = process(input)
    lines = []
    for line in data:
        l1, l2 = line.split(" -> ")
        x1, y1 = l1.split(",")
        x2, y2 = l2.split(",")
        if x1 == x2 or y1 == y2:
            lines.append(((int(x1), int(y1)), (int(x2), int(y2))))
    grid = {}
    for line in lines:
        x1, y1 = line[0]
        x2, y2 = line[1]
        if x1 == x2:
            for y in range(min(y1,y2), max(y1,y2)+1):
                grid[(x1, y)] = grid.get((x1, y), 0) + 1
        else:
            for x in range(min(x1,x2), max(x1,x2)+1):
                grid[(x, y1)] = grid.get((x, y1), 0) + 1

    return len([i for i in grid.values() if i > 1])

def p2(input):
    data = process(input)
    lines = []
    for line in data:
        l1, l2 = line.split(" -> ")
        x1, y1 = l1.split(",")
        x2, y2 = l2.split(",")
        lines.append(((int(x1), int(y1)), (int(x2), int(y2))))
    grid = {}
    for line in lines:
        x1, y1 = line[0]
        x2, y2 = line[1]
        if x1 == x2:
            for y in range(min(y1,y2), max(y1,y2)+1):
                grid[(x1, y)] = grid.get((x1, y), 0) + 1
        elif y1 == y2:
            for x in range(min(x1,x2), max(x1,x2)+1):
                grid[(x, y1)] = grid.get((x, y1), 0) + 1
        else:
            dx = 1 if x1 < x2 else -1
            dy = 1 if y1 < y2 else -1
            xs = range(x1, x2 + dx, dx)
            ys = range(y1, y2 + dy, dy)
            for i in range(len(xs)):
                grid[(xs[i], ys[i])] = grid.get((xs[i], ys[i]), 0) + 1

    return len([i for i in grid.values() if i > 1])

if sample_answer1:
    print("sample test", p1(sample_input) == sample_answer1)
    print("Problem1", p1(input))
if sample_answer2:
    print("sample test2", p2(sample_input) == sample_answer2)
    print("Problem2", p2(input))
