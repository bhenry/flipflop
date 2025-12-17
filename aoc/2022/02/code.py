import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """A Y
B X
C Z
"""

# key loses to value
rules = {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock",
}

translator = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}

values = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}

sample_answer1 = 15
sample_answer2 = 12

def score(line):
    a, b = line.strip().split(" ")
    a = translator[a]
    b = translator[b]
    your_shape = values[b]

    if rules[b] == a:
        result = 0 # loss
    if a == b:
        result = 3 # draw
    if rules[a] == b:
        result = 6 # win

    return result + your_shape

def process(input):
    scores = [score(line) for line in input.splitlines() if line]
    return sum(scores)

def p1(input):
    return process(input)

def score2(line):
    a, b = line.strip().split(" ")

    a = translator[a]
    b = {"X": rules[rules[a]], "Y": a, "Z": rules[a]}[b]
    your_shape = values[b]

    if rules[b] == a:
        result = 0 # loss
    if a == b:
        result = 3 # draw
    if rules[a] == b:
        result = 6 # win

    return result + your_shape

def process2(input):
    scores = [score2(line) for line in input.splitlines() if line]
    return sum(scores)

def p2(input):
    return process2(input)

if sample_answer1:
    print("sample test", p1(sample_input) == sample_answer1)
    print("Problem1", p1(input))
if sample_answer2:
    print("sample test2", p2(sample_input) == sample_answer2)
    print("Problem2", p2(input))
