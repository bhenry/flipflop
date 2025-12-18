import os
import sys
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
birds = [(nums(line), (0,0)) for line in lines]
for s in range(100):
    new_birds = []
    for bird in birds:
        (vx, vy), (x, y) = bird
        x += vx
        y += vy
        new_birds.append(((vx, vy), (x % 1000, y % 1000)))
    birds = new_birds

for bird in birds:
    (vx, vy), (x, y) = bird
    if x >= 250 and x < 750 and y >= 250 and y < 750:
        part1 += 1
print(part1)

part2 = 0
birds = [(nums(line), (0,0)) for line in lines]
for p in range(1000):
    new_birds = []
    for bird in birds:
        (vx, vy), (x, y) = bird
        x += vx * (p + 1) * 3600
        y += vy * (p + 1) * 3600
        new_pos = (x % 1000, y % 1000)
        new_birds.append(((vx, vy), new_pos))
        if new_pos[0] >= 250 and new_pos[0] < 750 and new_pos[1] >= 250 and new_pos[1] < 750:
            part2 += 1
print(part2)

part3 = 0
birds = [(nums(line), (0,0)) for line in lines]
for p in range(1000):
    new_birds = []
    for bird in birds:
        (vx, vy), (x, y) = bird
        x += vx * (p + 1) * 31556926
        y += vy * (p + 1) * 31556926
        new_pos = (x % 1000, y % 1000)
        new_birds.append(((vx, vy), new_pos))
        if new_pos[0] >= 250 and new_pos[0] < 750 and new_pos[1] >= 250 and new_pos[1] < 750:
            part3 += 1
print(part3)
