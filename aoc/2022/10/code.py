import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""

sample_answer1 = 13140
sample_answer2 = """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
"""

def process(input):
    return [i.strip() for i in input.splitlines()]

# print(process(sample_input))

def p1(input):
    data = process(input)
    cycles = 0
    x = 1
    totes = 0
    for inst in data:
        if inst.startswith("addx"):
            cycles += 1
            if cycles == 20 or (cycles - 20) % 40 == 0:
                totes += x*cycles
            cycles += 1
            if cycles == 20 or (cycles - 20) % 40 == 0:
                totes += x*cycles
            x += int(inst[5:])
        elif inst.startswith("noop"):
            cycles += 1
            if cycles == 20 or (cycles - 20) % 40 == 0:
                totes += x*cycles
    return totes

def draw(cycle, pos):
    return "##" if (cycle % 40) in [pos - 1, pos, pos + 1] else "  "

def p2(input):
    data = process(input)
    cycle = 0
    x = 1
    screen = ""
    for inst in data:
        if inst.startswith("addx"):
            screen = screen + draw(cycle, x)
            cycle += 1
            screen = screen + ("\n" if cycle % 40 == 0 else "")
            screen = screen + draw(cycle, x)
            cycle += 1
            screen = screen + ("\n" if cycle % 40 == 0 else "")
            x += int(inst[5:])
        elif inst.startswith("noop"):
            screen = screen + draw(cycle, x)
            cycle += 1
            screen = screen + ("\n" if cycle % 40 == 0 else "")
    return screen


if sample_answer1:
    print("sample test", p1(sample_input) == sample_answer1)
    print("Problem1", p1(input))
if sample_answer2:
    print("sample test2", p2(sample_input) == sample_answer2)
    print("Problem2")
    print(p2(input))
