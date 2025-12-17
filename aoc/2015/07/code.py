import os
import sys
APP_DIR = os.path.dirname(os.path.abspath(__file__).split("aoc")[0])
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

def process(pz):
    return pz.lines()

CACHE = {}
def parse(vals, data):
    if data in CACHE:
        return CACHE[data]
    if data.isnumeric():
        return int(data)
    elif v := vals.get(data.strip()):
        if v.isnumeric():
            return int(v)
        else:
            result = parse(vals, v)
            CACHE[data] = result
            return result
    elif " AND " in data:
        a, b = data.split(" AND ")
        return parse(vals, a) & parse(vals, b)
    elif " OR " in data:
        a, b = data.split(" OR ")
        return parse(vals, a) | parse(vals, b)
    elif " LSHIFT " in data:
        a, b = data.split(" LSHIFT ")
        return parse(vals, a) << parse(vals, b)
    elif " RSHIFT " in data:
        a, b = data.split(" RSHIFT ")
        return parse(vals, a) >> parse(vals, b)
    elif "NOT " in data:
        a = data.split("NOT ")[1]
        return 65535 - parse(vals, a)
    else:
        print("WTF", data)
        return None

def p1(pz):
    vals = {}
    for line in pz:
        data, target = line.split(" -> ")
        vals[target.strip()] = data.strip()

    for k in vals:
        print(k, parse(vals, vals[k]))

    return parse(vals, "a")

pzz = process(puzzleinput)

answer1 = p1(pzz)
print("\nproblem1", answer1, "\n\n")

CACHE = {"b": answer1}
answer2 = p1(pzz)
print("\nproblem2", answer2, "\n\n")
