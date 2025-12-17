import os
import sys
from itertools import combinations_with_replacement
from functools import cache
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import nums, rawfile
path_to_day = os.path.dirname(__file__)
raw = rawfile(f'{path_to_day}/input.txt')

lines = raw.split("\n")

sample = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""
lines = sample.strip().split("\n")

@cache
def push_button(state, button):
    new_state = list(state)
    for i in button:
        if new_state[i] == '.':
            new_state[i] = '#'
        else:
            new_state[i] = '.'
    return ''.join(new_state)

def find_min_buttons(lights, buttons):
    required_state = lights
    initial_state = '.' * len(lights)
    buttons = [tuple(nums(b)) for b in buttons]
    i = 1
    while True:
        for combo in combinations_with_replacement(buttons, i):
            current_state = initial_state
            for button in combo:
                current_state = push_button(current_state, button)
                if current_state == required_state:
                    return i
        i += 1
        if i > 1000000:
            break
    return -1000000

part1 = 0
for machine in lines:
    manual = machine.split(" ")
    lights = manual.pop(0)[1:-1]
    joltage = manual.pop()[1:-1]
    buttons = manual
    part1 += find_min_buttons(lights,buttons)
print(part1)

part2 = 0
for machine in lines:
    manual = machine.split(" ")
    lights = manual.pop(0)[1:-1]
    joltage = [int(x) for x in manual.pop()[1:-1].split(",")]
    buttons = map(nums, manual)

    print(lights, joltage, list(buttons))

print(part2)
