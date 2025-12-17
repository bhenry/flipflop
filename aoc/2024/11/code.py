import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import Input, nums
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

line = puzzleinput.lines()[0]

sample = """
"""
# lines = sample.strip().split("\n")

part1 = 0

ns = nums(line)

for i in range(25):
    b = []
    for n in ns:
        if n == 0:
            b.append(1)
            continue
        if len(str(n)) % 2 == 0:
            left = str(n)[:len(str(n))//2]
            right = str(n)[len(str(n))//2:]
            b.append(int(left))
            b.append(int(right))
            continue
        b.append(n*2024)
    ns = b

print(len(ns))

part2 = 0

ns = nums(line)

c = {}
def stones(n, r):
    if (n, r) in c: return c[(n, r)]
    if r == 0: return 1
    if n == 0: return stones(1, r-1)
    if len(str(n)) % 2 == 0:
        left = str(n)[:len(str(n))//2]
        right = str(n)[len(str(n))//2:]
        new = stones(int(left), r-1) + stones(int(right), r-1)
        c[(n, r)] = new
        return new
    return stones(n*2024, r-1)

print(sum(stones(n, 75) for n in ns))
