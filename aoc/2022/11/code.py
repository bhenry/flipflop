import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""

def mult(operand):
    if operand.isdigit():
        return lambda x: x * int(operand)
    else:
        return lambda x: x ** 2

class Monkey():
    def __init__(self, monkey_string):
        self.monkey_string = monkey_string
        self.id = int(monkey_string.splitlines()[0].split()[1][0])
        self.items = self._items()
        self.operation = self._operation()
        self.test = self._test()
        self.conditions = self.test_conditions()
        self.inspections = 0
        self.themod = int(self.monkey_string.splitlines()[3].split(":")[1].strip().split()[-1])

    def __repr__(self):
        return f"{self.monkey_string.splitlines()[0]}, {self.inspections}"

    def _items(self):
        return [int(i) for i in self.monkey_string.splitlines()[1].split(":")[1].strip().split(",")]

    def _operation(self):
        operation = self.monkey_string.splitlines()[2].split(":")[1].strip()
        operator = operation.split()[-2]
        operand = operation.split()[-1]
        if operator == "*":
            return mult(operand)
        elif operator == "+":
            return lambda x: x + (int(operand) if operand.isdigit() else x)

    def _test(self):
        test = self.monkey_string.splitlines()[3].split(":")[1].strip()
        return lambda x: x % int(test.split()[-1]) == 0

    def test_conditions(self):
        tf = self.monkey_string.splitlines()[4:]
        return [int(i.split()[-1]) for i in tf]

    def additem(self, item):
        self.items.append(item)

    def dothings(self, monkeys):
        for item in self.items:
            self.inspections += 1
            o = self.operation(item)
            n = o // 3
            if self.test(n):
                # print(f"add {n} to monkey {self.conditions[0]}")
                monkeys[self.conditions[0]].additem(n)
            else:
                # print(f"add {n} to monkey {self.conditions[1]}")
                monkeys[self.conditions[1]].additem(n)
        self.items = []

    def dothings2(self, monkeys):
        for item in self.items:
            self.inspections += 1
            o = self.operation(item)
            n = o #// 3
            if self.test(n):
                # print(f"add {n} to monkey {self.conditions[0]}")
                monkeys[self.conditions[0]].additem(n)
            else:
                # print(f"add {n} to monkey {self.conditions[1]}")
                monkeys[self.conditions[1]].additem(n)
        self.items = []

sample_answer1 = 10605
sample_answer2 = 2713310158

def process(input):
    return [i for i in input.split("\n\n")]

def p1(input):
    monkeys = [Monkey(m) for m in process(input)]
    for round in range(20):
        for m in monkeys:
            m.dothings(monkeys)
    scores = [m.inspections for m in monkeys]
    scores.sort()
    return scores[-1] * scores[-2]

def p2(input):
    monkeys = [Monkey(m) for m in process(input)]
    divider = 1
    for m in monkeys:
        divider *= m.themod
    for round in range(10000):
        for m in monkeys:
            m.items = [i % divider for i in m.items]
            m.dothings2(monkeys)
    scores = [m.inspections for m in monkeys]
    scores.sort()
    return scores[-1] * scores[-2]


if sample_input.strip():
    sample_result = p1(sample_input)
    print("sample1 test", sample_answer1 and (sample_result == sample_answer1))
    print("sample1", p1(sample_input))
    print("Problem1", p1(input), "\n\n")
if sample_answer2:
    sample_result = p2(sample_input)
    print("sample2 test", sample_answer2 and (sample_result == sample_answer2))
    print("sample2", p2(sample_input))
    print("Problem2", p2(input))
