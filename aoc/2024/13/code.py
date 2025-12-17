import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import Input, nums
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

machines = "\n".join(puzzleinput.lines()).split("\n\n")

sample = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""
machines = sample.strip().split("\n\n")
# 3t for A button 1t for B button

part1 = 0

for machine in machines:
    lines = machine.split("\n")
    ax,ay = nums(lines[0])
    bx,by = nums(lines[1])
    px,py = nums(lines[2])

    # solve for an in ax*an + bx*bn == px and ay*an + by*bn == py
    an = (px - bx*bn) / ax
    bn = (py - ay*an) / by
    gcf = 1
    for i in range(1, int(max(an,bn))):
        if an % i == 0 and bn % i == 0:
            gcf = i
    an = int(an / gcf)


    x = prize[0]
    y = prize[1]

    if x < button_a[0] or x > button_b[0] or y < button_a[1] or y > button_b[1]:
        part1 += 1

part2 = 0
