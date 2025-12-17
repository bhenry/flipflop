import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
"""

sample_answer2 = 301

def process(input):
    return [i.strip() for i in input.splitlines()]

# print(process(sample_input))
MONKEYS = {}
class monkey():
    def __init__(self, inputt):
        self.id = inputt.split(":")[0]
        v = inputt.split(":")[1].strip()
        self.value = v


    def do(self):
        parts = self.value.split(" ")
        if self.id == "humn":
            return "x"
        if len(parts) == 1:
            return int(self.value)
        p1 = MONKEYS[parts[0]].do()
        p2 = MONKEYS[parts[2]].do()
        if self.id == "root":
            return f"{p1} == {p2}"
        if isinstance(p1, str) or isinstance(p2, str):
            return f"({p1} {parts[1]} {p2})"
        if parts[1] == "+":
            return p1 + p2
        elif parts[1] == "-":
            return p1 - p2
        elif parts[1] == "*":
            return p1 * p2
        elif parts[1] == "/":
            return p1 / p2


def p2(input):
    data = process(input)
    for i in data:
        MONKEYS[i.split(":")[0]] = monkey(i)
    equation = MONKEYS['root'].do()

if sample_answer2:
    sample_result = p2(sample_input)
    print("sample2", sample_result)
    if sample_result == sample_answer2:
        print("sample2 test pass")
print("\nproblem2", p2(input), "\n\n")


print("\ndone")

"""
((691 + ((817.0 + (6259659210072.0 - ((10 + (((((875.0 + (308 + ((((((2 * (((683.0 + ((((2 * ((((((2 * ((((((2 * (((((((((((((((((11 * (810.0 + (((((((813.0 + (92.0 * (((251 + ((((x - 611) * 4) + 930.0) / 6)) / 2) - 198))) + 473) / 3) - 477) * 2) - 209) / 7))) - 213) * 2) + 387.0) + 733) / 2) + 921) * 2) - 380) / 6) + 335.0) / 6) - 715) * 21) + 436) / 2) - 260)) - 646.0) * 2) + 623) / 3) - 115.0)) + 714.0) / 2) + 787.0) / 2) - 300.0)) - 592) * 2) + 599)) / 2) - 421.0)) + 511.0) / 3) - 275) * 2) + 897))) / 12) + 711) * 3) - 635.0)) / 7))) / 2)) * 19) == 21608329599731.0
"""
