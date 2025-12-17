from copy import deepcopy
import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """1
2
-3
3
-2
0
4
"""

sample_answer1 = 3
sample_answer2 = 1623178306

def process(input):
    return [int(i.strip()) for i in input.splitlines()]

def p1(input):
    data = []
    for i,v in enumerate(process(input)):
        data.append((i,v))
        if v == 0:
            zero = (i,v)
    divider = len(data) - 1
    copy = deepcopy(data)
    for i,v in copy:
        if v == 0:
            continue
        curloc = data.index((i,v))
        newloc = curloc + v
        newloc = newloc % divider
        moving = data.pop(curloc)
        data.insert(newloc%divider, moving)
    zeroth = data.index(zero)
    thousandthafterzero = data[(zeroth+1000)%len(data)]
    twothousandthafterzero = data[(zeroth+2000)%len(data)]
    threethousandthafterzero = data[(zeroth+3000)%len(data)]
    return thousandthafterzero[1] + twothousandthafterzero[1] + threethousandthafterzero[1]

def p2(input):
    decrypt = 811589153
    data = []
    for i,v in enumerate(process(input)):
        data.append((i,v*decrypt))
        if v == 0:
            zero = (i,v)
    divider = len(data) - 1
    copy = deepcopy(data)
    for _ in range(10):
        for i,v in copy:
            if v == 0:
                continue
            curloc = data.index((i,v))
            newloc = curloc + v
            newloc = newloc % divider
            moving = data.pop(curloc)
            data.insert(newloc%divider, moving)
    zeroth = data.index(zero)
    thousandthafterzero = data[(zeroth+1000)%len(data)]
    twothousandthafterzero = data[(zeroth+2000)%len(data)]
    threethousandthafterzero = data[(zeroth+3000)%len(data)]
    return thousandthafterzero[1] + twothousandthafterzero[1] + threethousandthafterzero[1]

if sample_answer1:
    sample_result = p1(sample_input)
    print("sample1", sample_result)
    if sample_result == sample_answer1:
        print("sample1 test pass")
        print("\nproblem1", p1(input), "\n\n")

if sample_answer2:
    sample_result = p2(sample_input)
    print("sample2", sample_result)
    if sample_result == sample_answer2:
        print("sample2 test pass")
        print("\nproblem2", p2(input), "\n\n")


print("\ndone")
