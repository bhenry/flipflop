import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

lines = puzzleinput.lines()

def safe(nums):
    if nums == sorted(nums) or nums == sorted(nums, reverse=True):
        x = nums[0]
        for y in nums[1:]:
            if (y > x and y - x > 3) or (y < x and x - y > 3) or y - x == 0:
                return False
            x = y
        return True
    return False

part1 = len([line for line in lines if safe([int(n) for n in line.split()])])

print(part1)

part2 = 0

for line in lines:
    unsafe = 0
    nums = [int(n) for n in line.split()]
    if safe(nums):
        part2 += 1
    else:
        for i in range(len(nums)):
            nms = nums.copy()
            nms.pop(i)
            if safe(nms):
                part2 += 1
                break

print(part2)
