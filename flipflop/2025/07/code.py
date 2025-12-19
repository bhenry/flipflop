import os
import sys
from math import comb, factorial
APP_DIR = os.path.abspath(__file__).split("flipflop")[0]
sys.path.append(APP_DIR)
from lib.util import nums, rawfile
path_to_day = os.path.dirname(__file__)
raw = rawfile(f'{path_to_day}/input.txt')

lines = raw.split("\n")

sample = """
"""
# lines = sample.strip().split("\n")

part1 = 0
for line in lines:
    x,y = nums(line)
    part1 += comb(x-1+y-1, y-1)
print(part1)

part2 = 0
for line in lines:
    x,y = nums(line)
    part2 += factorial((x-1)+(y-1)+(x-1))//(factorial(y-1)*factorial(x-1)*factorial(x-1))
print(part2)

part3 = 0
for line in lines:
    x,y = nums(line)
    part3 += factorial((y-1)*x)//(factorial(y-1)**x)
print(part3)
