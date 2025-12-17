import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """forward 5
down 5
forward 8
up 3
down 8
forward 2
"""

sample_answer1 = 150
sample_answer2 = 900

def process(input):
    return [i.strip() for i in input.splitlines()]

print(process(sample_input))

def p1(input):
    instructions = process(input)
    x, y = 0, 0
    for step in instructions:
        direction, distance = step.split()
        distance = int(distance)
        if direction == "forward":
            x += distance
        elif direction == "down":
            y += distance
        elif direction == "up":
            y -= distance
    return x*y

def p2(input):
    data = process(input)
    x, y, a = 0, 0, 0
    for step in data:
        direction, distance = step.split()
        distance = int(distance)
        if direction == "forward":
            x += distance
            y += a * distance
        elif direction == "down":
            a += distance
        elif direction == "up":
            a -= distance
    return x*y

if sample_answer1:
    print("sample test", p1(sample_input) == sample_answer1)
    print("Problem1", p1(input))
if sample_answer2:
    print("sample test2", p2(sample_input) == sample_answer2)
    print("Problem2", p2(input))
