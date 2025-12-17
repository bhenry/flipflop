from curses.ascii import isdigit
import functools
import json
import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""

sample_answer1 = 13
sample_answer2 = 140

def process(input):
    return input.split("\n\n")

def compare(a,b):
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return -1
        if a > b:
            return 1
        if a == b:
            return 0
    if isinstance(a, list) and isinstance(b, list):
        for i in range(max(len(a), len(b))):
            if i >= len(a):
                return -1
            if i >= len(b):
                return 1
            if c := compare(a[i], b[i]):
                return c
            i += 1
        return 0
    if not isinstance(a, list) and isinstance(b, list):
        return compare([a], b)
    if isinstance(a, list) and not isinstance(b, list):
        return compare(a, [b])


def p1(input):
    pairs = process(input)
    inorder = []
    for i, pair in enumerate(pairs):
        l,r = [json.loads(x) for x in pair.strip().split("\n")]
        if compare(l,r) == -1:
            inorder.append(i+1)
    return sum(inorder)

def p2(input):
    data = [json.loads(i) for i in input.split()]
    data.append([[2]])
    data.append([[6]])
    ans = 1
    for i, v in enumerate(sorted(data, key=functools.cmp_to_key(compare))):
        if v == [[2]]:
            ans *= i+1
        if v == [[6]]:
            ans *= i+1
    return ans

if sample_answer1:
    sample_result = p1(sample_input)
    print("sample1 test", sample_result == sample_answer1)
    print("sample1", sample_result)
    if sample_result == sample_answer1:
        print("\nproblem1", p1(input), "\n\n")

if sample_answer2:
    sample_result = p2(sample_input)
    print("sample2 test", sample_result == sample_answer2)
    print("sample2", p2(sample_input))
    if sample_result == sample_answer2:
        print("\nproblem2", p2(input), "\n\n")
