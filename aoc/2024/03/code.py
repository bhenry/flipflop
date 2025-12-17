import os
import sys
import re

APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

lines = puzzleinput.lines()

part1 = 0
for line in lines:
    ops = re.findall("mul\((\d+,\d+)\)", line)
    for op in ops:
        a, b = map(int, op.split(","))
        part1 += a * b

print(part1)

part2 = 0

enabled = True
for line in lines:
    ops = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", line)
    for op in ops:
        print(op)
        if "do" in op:
            enabled = True
        if "don't" in op:
            enabled = False
        if enabled and "mul" in op:
            a, b = map(int, op[4:-1].split(","))
            part2 += a * b

print(part2)
