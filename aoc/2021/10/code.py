from collections import defaultdict
import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

sample_input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""

sample_answer1 = 26397
sample_answer2 = 288957

def process(input):
    return [i.strip() for i in input.splitlines()]

def p1(input):
    data = process(input)
    closes = {")": "(", "]": "[", "}": "{", ">": "<"}
    tally = defaultdict(int)
    for line in data:
        opens = []
        for char in line:
            if char in "([{<":
                opens.append(char)
            elif char in ")]}>":
                lastopener = opens[-1]
                charopener = closes[char]
                if lastopener != charopener:
                    tally[char] += 1
                    break
                else:
                    opens.pop()
    return sum([tally[char] * scores[char] for char in tally])

def calculate_score(opens):
    points = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    score = 0
    cs = {"(": ")", "[": "]", "{": "}", "<": ">"}
    opens.reverse()
    for char in opens:
        score = score*5 + points[cs[char]]
    return score

def p2(input):
    data = process(input)

    os = {")": "(", "]": "[", "}": "{", ">": "<"}
    tally = []
    scores = []
    for line in data:
        opens = []
        ignore = False
        for char in line:
            if char in "([{<":
                opens.append(char)
            elif char in ")]}>":
                lastopener = opens[-1]
                charopener = os[char]
                if lastopener != charopener:
                    ignore = True
                    break
                else:
                    opens.pop()
        if not ignore:
            score = calculate_score(opens)
            scores.append(score)
    return sorted(scores)[len(scores)//2]

if sample_answer1:
    sample_result = p1(sample_input)
    print("sample1 test", sample_result == sample_answer1)
    print("sample1", sample_result)
    if sample_result == sample_answer1:
        print("\nproblem1", p1(input), "\n\n")

if sample_answer2:
    sample_result = p2(sample_input)
    print("sample2 test", sample_result == sample_answer2)
    print("sample2", sample_result)
    if sample_result == sample_answer2:
        print("\nproblem2", p2(input), "\n\n")
