import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import nums, rawfile
path_to_day = os.path.dirname(__file__)
raw = rawfile(f'{path_to_day}/input.txt')

lines = raw.split("\n")

sample = """
"""
# lines = sample.strip().split("\n")

def invalid(n):
    s = str(n)
    l = len(s)
    s1 = s[:l//2]
    s2 = s[l//2:]
    return s1 == s2

part1 = 0
ranges = lines[0].split(",")
for r in ranges:
    a,b = r.split("-")
    a = int(a)
    b = int(b)
    for i in range(a, b+1):
        if invalid(i):
            part1 += i

print(part1)

def invalid2(n):
    s = str(n)
    l = len(s)
    for i in range(1, l):
        s1 = s[:i]
        if s == s1 * (l // i):
            return True

part2 = 0
for r in ranges:
    a,b = r.split("-")
    a = int(a)
    b = int(b)
    for i in range(a, b+1):
        if invalid2(i):
            part2 += i

print(part2)
