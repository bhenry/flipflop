import os
import string
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

sample_answer1 = 157
sample_answer2 = 70

def process(input):
    return [i.strip() for i in input.splitlines()]

alphabet = list(string.ascii_lowercase)
ALPHABET = list(string.ascii_uppercase)
priority = {alphabet[i]: i+1 for i in range(len(alphabet))}
priority.update({ALPHABET[i]: i+27 for i in range(len(ALPHABET))})

def p1(input):
    sax = process(input)
    s = 0
    for sac in sax:
        c1, c2 = sac[:len(sac)//2], sac[len(sac)//2:]
        repeat = set(c1).intersection(set(c2))
        s += priority[repeat.pop()]
    return s

def p2(input):
    sax = process(input)
    s = 0
    groups = [sax[i:i + 3] for i in range(0, len(sax), 3)]
    for group in groups:
        common = set(group[0]).intersection(set(group[1])).intersection(set(group[2]))
        s += priority[common.pop()]
    return s

if sample_answer1:
    print("sample test", p1(sample_input) == sample_answer1)
    print("Problem1", p1(input))
if sample_answer2:
    print("sample test2", p2(sample_input) == sample_answer2)
    print("Problem2", p2(input))
