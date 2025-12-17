import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import Input, nums
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

lines = "\n".join(puzzleinput.lines()).split("\n\n")

sample = """
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""
# lines = sample2.strip().split("\n\n")

part1 = 0

register = {}

for r in lines[0].split("\n"):
    reg = r.split(":")[0][-1]
    val = int(r.split(":")[1].strip())
    register[reg] = val

def convertop(op):
    if op <= 3:
        return op
    if op == 4:
        return register["A"]
    if op == 5:
        return register["B"]
    if op == 6:
        return register["C"]
    else:
        raise Exception("Invalid operand")

def resetRegister(initA):
    register["A"] = initA
    register["B"] = 0
    register["C"] = 0

def perform(func):
    output = []
    program = func
    i = 0
    while True:
        if i >= len(program):
            break
        instr = program[i]
        operand = program[i+1]
        combo = convertop(operand)
        if instr == 0:
            register["A"] = int(register["A"] / (2**combo))
        if instr == 1:
            x,y = register["B"],operand
            register["B"] = ((x | y) & (~x | ~y))
        if instr == 2:
            register["B"] = combo % 8
        if instr == 3:
            if register["A"] != 0:
                i = operand
                continue
        if instr == 4:
            x = register["B"]
            y = register["C"]
            register["B"] = ((x | y) & (~x | ~y))
        if instr == 5:
            output.append(combo % 8)
        if instr == 6:
            register["B"] = int(register["A"] / (2**combo))
        if instr == 7:
            register["C"] = int(register["A"] / (2**combo))
        i += 2
    return output

print(",".join(str(o) for o in perform(nums(lines[1]))))

sample2 = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
"""
# lines = sample2.strip().split("\n\n")

inp = nums(lines[1])
initA = 0
while True:
    resetRegister(initA)
    output = perform(inp)
    if output[:4] == inp[:4]:
        print(initA)
    if output == inp:
        print(initA)
        break
    else:
        initA += 1

print(initA)
