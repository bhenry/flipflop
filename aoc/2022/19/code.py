import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.
"""

sample_answer1 = 33
sample_answer2 = None

def process(input):
    return [i.strip() for i in input.strip().split("\n")]

# print(process(sample_input))

class blueprint():
    def __init__(self, b) -> None:
        self.text = b
        self.name = b.split(":")[0]
        self.id = int(self.name.split()[1])
        costs = b.split(":")[1].strip().split(".")[:-1]
        self.costs = {}
        for cost in costs:
            self.costs[cost.split()[1]] = self.parsecost(cost)


    @staticmethod
    def parsecost(cost):
        c = cost[cost.find("costs ")+6:].rstrip(".").split(" and ")
        return {i.split()[1]:int(i.split()[0]) for i in c}


    def __repr__(self) -> str:
        return f"{self.name}: {self.costs}"

    def affordable(self, inventory):
        affordable = {}
        for item in self.costs:
            if item in inventory:
                affordable[item] = inventory[item]//self.costs[item]
        return affordable

    def maxscore(self, inventory):
        affordable = self.affordable(inventory)
        if not affordable:
            return 0
        minaffordable = min(affordable.values())
        for item in affordable:
            inventory[item] -= minaffordable*self.costs[item]
        inventory["geodes"] += minaffordable
        return minaffordable + self.maxscore(inventory)

def maxscore(b):
    inventory = {}
    inventory["geodes"] = 0
    inventory["ore"] = 0
    inventory["clay"] = 0
    inventory["obsidian"] = 0
    inventory["geode robots"] = 0
    inventory["ore robots"] = 1
    inventory["clay robots"] = 0
    inventory["obsidian robots"] = 0

    return b.maxscore(inventory)

def p1(input):
    data = process(input)
    blueprints = [blueprint(b) for b in data]
    # every minute calculate everything you can afford. add to set of options.
    # for each option in the next minute, calculate everything you can afford.
    # recursively maximize geodes
    bpscores = {}
    for b in blueprints:
        bpscores[b.id] = maxscore(b)
    return sum(b.id*s for s in bpscores)

def p2(input):
    data = process(input)
    return data

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
