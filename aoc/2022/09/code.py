import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

sample_answer1 = 13
sample_answer2 = 1

def process(input):
    return [i.strip() for i in input.splitlines()]

def move(dir, dist):
    if dir == 'R':
        return (dist, 0)
    if dir == 'L':
        return (-dist, 0)
    if dir == 'U':
        return (0, dist)
    if dir == 'D':
        return (0, -dist)

def newtail(h, t):
    if abs(t[0] - h[0]) > 1 and abs(t[1] - h[1]) > 1:
        return (h[0] - 1 if t[0] < h[0] else h[0] + 1, h[1] - 1 if t[1] < h[1] else h[1] + 1)
    if abs(t[0] - h[0]) > 1:
        return (h[0] - 1 if t[0] < h[0] else h[0] + 1, h[1])
    if abs(t[1] - h[1]) > 1:
        return (h[0], h[1] - 1 if t[1] < h[1] else h[1] + 1)
    return t

def p1(input):
    data = process(input)
    h = (0,0)
    t = (0,0)
    tspots = set([(0,0)])
    for m in data:
        dir, dist = m.split()
        for d in range(int(dist)):
            mv = move(dir, 1)
            h = (h[0] + mv[0], h[1] + mv[1])
            t = newtail(h, t)
            tspots.add(t)
    return (len(tspots))

def p2(input):
    data = process(input)
    h = (0,0)
    tzones = set([(0,0)])
    tails = [(0,0) for i in range(9)]
    for m in data:
        dir, dist = m.split()
        for d in range(int(dist)):
            mv = move(dir, 1)
            h = (h[0] + mv[0], h[1] + mv[1])
            t1 = newtail(h, tails[0])
            t2 = newtail(t1, tails[1])
            t3 = newtail(t2, tails[2])
            t4 = newtail(t3, tails[3])
            t5 = newtail(t4, tails[4])
            t6 = newtail(t5, tails[5])
            t7 = newtail(t6, tails[6])
            t8 = newtail(t7, tails[7])
            t9 = newtail(t8, tails[8])
            tails = [t1, t2, t3, t4, t5, t6, t7, t8, t9]
            tzones.add(t9)
    return (len(tzones))

if sample_answer1:
    print("sample test", p1(sample_input) == sample_answer1)
    print("Problem1", p1(input))
if sample_answer2:
    print("sample test2", p2(sample_input) == sample_answer2)
    print("Problem2", p2(input))
