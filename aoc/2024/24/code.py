import os
import sys
APP_DIR = os.path.abspath(__file__).split("aoc")[0]
sys.path.append(APP_DIR)
from lib.util import nums, rawfile
path_to_day = os.path.dirname(__file__)
raw = rawfile(f'{path_to_day}/input.txt')

init,andthen = raw.split("\n\n")

sample = """
x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
"""
# init,andthen = sample.strip().split("\n\n")

starting = {}
for line in init.split("\n"):
    k,v = line.split(": ")
    starting[k] = int(v)

logic = {}
for line in andthen.split("\n"):
    a,b = line.split(" -> ")
    logic[b] = a.split(" ")

part1 = 0
c = {}
def calc(wire):
    if wire in c:
        return c[wire]
    if wire in starting:
        return starting[wire]
    a,op,b = logic[wire]
    if op == "AND":
        c[wire] = calc(a) and calc(b)
    if op == "OR":
        c[wire] = calc(a) or calc(b)
    if op == "XOR":
        c[wire] = calc(a) ^ calc(b)
    return c[wire]


for w in logic:
    if w.startswith("z"):
        print(calc(w))
        # part1 += calc(w)*2^int(w[1:])



print(list(enumerate(c[w] for w in sorted(c) if w.startswith("z"))))
for i,v in enumerate(c[w] for w in sorted(c) if w.startswith("z")):
    part1 += v*2**i
print(part1)
part2 = 0
