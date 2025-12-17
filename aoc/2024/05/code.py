import os
import sys
import re
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

lines = puzzleinput.input

sample = """47|53\n97|13\n97|61\n97|47\n75|29\n61|13\n75|53\n29|13\n97|29\n53|29\n61|53
97|53\n61|29\n47|13\n75|47\n97|75\n47|61\n75|61\n47|29\n75|13\n53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""
# lines = sample.strip()

part1 = 0
rules = {}  # {before: [after]}
for line in lines.split("\n\n")[0].splitlines():
    rule = [int(d) for d in re.findall("\d+", line)]
    rules[rule[0]] = [rule[1]] if rule[0] not in rules else rules[rule[0]] + [rule[1]]

def valid(ns):
    v = True
    for n in ns:
        if n not in rules:
            continue
        for r in rules[n]:
            if r not in ns:
                continue
            if ns.index(r) < ns.index(n):
                v = False
                break
        if not v:
            break
    return v

for line in lines.split("\n\n")[1].splitlines():
    ns = [int(n) for n in line.split(",")]
    if valid(ns):
        part1 += ns[int(len(ns)/2 - 0.5)]

print(part1)


part2 = 0
rules2 = {}  # {after: [before]}
for line in lines.split("\n\n")[0].splitlines():
    rule = [int(d) for d in re.findall("\d+", line)]
    rules2[rule[1]] = [rule[0]] if rule[1] not in rules2 else rules2[rule[1]] + [rule[0]]

def reorder(ns):
    new = []
    olen = len(ns)

    while ns:
        n = ns.pop(0)
        if n not in rules2:
            new.append(n)
            continue
        broke_rule = False
        for r in rules2[n]:
            if r in ns:
                ns.append(n)
                break
        else:
            new.append(n)

    return new

for line in lines.split("\n\n")[1].splitlines():
    ns = [int(n) for n in line.split(",")]
    if not valid(ns):
        new = reorder(ns.copy())
        part2 += new[int(len(new)/2 - 0.5)]

print(part2)
