import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import nums, rawfile
path_to_day = os.path.dirname(__file__)
raw = rawfile(f'{path_to_day}/input.txt')

lines = raw.split("\n")

sample = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
"""
# lines = sample.strip().split("\n")

storage = {}
for line in lines:
    a,b = line.split("-")
    if a in storage:
        storage[a].append(b)
    else:
        storage[a] = [b]
    if b in storage:
        storage[b].append(a)
    else:
        storage[b] = [a]

results = set()
for key in storage:
    for v in storage[key]:
        for k in storage[v]:
            if k in storage[key]:
                if [s for s in [key, v, k] if s.startswith("t")]:
                    results.add(tuple(sorted((key, v, k))))

print(len(results))

lans = set()

def collect(c, lan):
    k = ",".join(sorted(lan))
    if k in lans: return
    lans.add(k)
    for cx in storage[c]:
        if cx in lan: continue
        for cpu in lan:
            if cx not in storage[cpu]:
                break
        else:
            collect(cx, lan + [cx])

for node in storage:
    collect(node, [node])

print(max(lans, key=len))
