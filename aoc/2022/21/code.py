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

sample_answer1 = 152
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
        if len(parts) == 1:
            value = int(self.value)
        else:
            p1 = MONKEYS[parts[0]].do()
            p2 = MONKEYS[parts[2]].do()
            if parts[1] == "+":
                value = p1 + p2
            elif parts[1] == "-":
                value = p1 - p2
            elif parts[1] == "*":
                value = p1 * p2
            elif parts[1] == "/":
                value = p1 / p2
        return value


def p1(input):
    data = process(input)
    for i in data:
        MONKEYS[i.split(":")[0]] = monkey(i)
    return MONKEYS['root'].do()

def p2(input):
    data = process(input)
    for i in data:
        MONKEYS[i.split(":")[0]] = monkey(i)
    return MONKEYS['root'].do()

if sample_answer1:
    sample_result = p1(sample_input)
    print("sample1", sample_result)
    if sample_result == sample_answer1:
        print("sample1 test pass")
        print("\nproblem1", p1(input), "\n\n")

if sample_answer2:
    sample_result = p2(sample_input)
    print("sample2", sample_result)
    if sample_result == sample_answer2:
        print("sample2 test pass")
        print("\nproblem2", p2(input), "\n\n")


print("\ndone")
