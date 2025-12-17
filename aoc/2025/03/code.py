import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import nums, rawfile
path_to_day = os.path.dirname(__file__)
raw = rawfile(f'{path_to_day}/input.txt')

lines = raw.split("\n")

sample = """987654321111111
811111111111119
234234234234278
818181911112111
"""
# lines = sample.strip().split("\n")

part1 = 0
for line in lines:
    digits = [int(d) for d in line]
    first_digit = max(digits[:-1])
    digloc = digits.index(first_digit)
    second_digit = max(digits[digloc+1:])
    part1 += 10*first_digit + second_digit
print(part1)

part2 = 0
for line in lines:
    digits = [int(d) for d in line]
    ans = 0
    for i in range(11,-1,-1):
        if i == 0:
            highest = max(digits)
        else:
            highest = max(digits[:-i])
        digloc = digits.index(highest)
        digits = digits[digloc+1:]
        ans += highest * (10 ** i)
    part2 += ans
print(part2)
