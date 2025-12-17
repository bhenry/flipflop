import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

def process(input, n):
    data = input.splitlines()[0].strip()
    initial = data[0:n]
    for i, l in enumerate(data[n:]):
        if len(set(initial)) == n:
            return i + n
        initial = initial[1:] + l

def p1(input):
    return process(input, 4)

def p2(input):
    return process(input, 14)

print("Problem1", p1(input))
print("Problem2", p2(input))
