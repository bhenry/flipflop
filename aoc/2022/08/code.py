import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """30373
25512
65332
33549
35390
"""

sample_answer1 = 21
sample_answer2 = 8

def process(input):
    return [i.strip() for i in input.splitlines()]

def p1(input):
    data = process(input)
    side = [c for c in data[0]]
    trees = {}
    for i in range(len(data)):
        for line in data[1:]:
            side[i] += line[i]
    for x in range(len(data)):
        for y in range(len(side)):
            if not data[x][:y] or max(data[x][:y]) < data[x][y] or not data[x][y+1:] or max(data[x][y+1:]) < data[x][y]:
                trees[(x, y)] = True
            if not side[x][:y] or max(side[x][:y]) < side[x][y] or not side[x][y+1:] or max(side[x][y+1:]) < side[x][y]:
                trees[(y, x)] = True
    return len(trees.values())

def p2(input):
    data = process(input)
    trees = {}
    scores = {}
    for y in range(len(data)):
        for x in range(len(data[0])):
            trees[(x, y)] = data[y][x]

    for x, y in trees:
        tree = trees[(x, y)]
        lscore = 0
        ltrees = []
        if (x,y) == (2,3):
            pass
        for i in range(1, x+1):
            lscore += 1
            ltrees.append((x-i, y))
            if trees[(x-i, y)] < tree:
                continue
            else:
                break
        rscore = 0
        rtrees = []
        for i in range(x+1, len(data)):
            rtrees.append((i, y))
            rscore += 1
            if trees[(i, y)] < tree:
                continue
            else:
                break
        uscore = 0
        utrees = []
        for i in range(1, y + 1):
            uscore += 1
            utrees.append((x, y-i))
            if trees[(x, y-i)] < tree:
                continue
            else:
                break
        dscore = 0
        dtrees = []
        for i in range(y+1, len(data)):
            dscore += 1
            dtrees.append((x, i))
            if trees[(x, i)] < tree:
                continue
            else:
                break
        vscore = lscore * rscore * uscore * dscore
        scores[(x, y)] = vscore
    return(max(scores.values()))

if sample_answer1:
    print("sample test", p1(sample_input) == sample_answer1)
    print("Problem1", p1(input))
if sample_answer2:
    print("sample test2", p2(sample_input) == sample_answer2)
    print("Problem2", p2(input))
