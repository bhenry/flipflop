import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
"""

sample_answer1 = 1651
sample_answer2 = 1707
class Valve():
    def __init__(self, line):
        self.name = line.split(" ")[1]
        self.flow_rate = int(line.split("=")[1].split(";")[0])
        self.tunnels = [t.strip(',') for t in line.split(' ')[line.split(' ').index('to') + 2:]]

    def __repr__(self):
        return f"{self.name} {self.flow_rate} {self.tunnels}"

STORE = dict() # (pos, time_remaining, open_valves): flowscore
VALVES = dict()

def key(v, t, opens):
    return (v, t, "".join(sorted(opens)))

def compute(v, time, opened):
    if key(v, time, opened) in STORE:
        return STORE[key(v, time, opened)]
    if time < 0:
        return 0
    highest = 0
    valve = VALVES[v]
    if v not in opened:
        flow = valve.flow_rate * (time-1)
        for tunnel in valve.tunnels:
            if flow:
                highest = max(highest, flow + compute(tunnel, time-2, opened | set([v])))
            highest = max(highest, compute(tunnel, time-1, opened))
    else:
        # already open, so just passing through
        for tunnel in valve.tunnels:
            highest = max(highest, compute(tunnel, time-1, opened))
    STORE[key(v, time, opened)] = highest
    return highest

def process(input):
    VALVES.clear()
    STORE.clear()
    for i in input.strip().splitlines():
        VALVES[i.split(" ")[1]] = Valve(i)

# print(process(sample_input))

def p1(input):
    process(input)
    return compute('AA', 30, set())

def p2(input):
    data = process(input)
    return compute('AA', 30, set())

# if sample_answer1:
#     sample_result = p1(sample_input)
#     print("sample1", sample_result)
#     if sample_result == sample_answer1:
#         print("sample1 test pass")
# print("\nproblem1", p1(input), "\n\n")

if sample_answer2:
    sample_result = p2(sample_input)
    print("sample2", sample_result)
    if sample_result == sample_answer2:
        print("sample2 test pass")
        print("\nproblem2", p2(input), "\n\n")


print("\ndone")
