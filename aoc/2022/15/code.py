import os
import re
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""

sample_answer1 = 26
sample_answer2 = 56000011

def process(input):
    return [i.strip() for i in input.strip().split("\n")]

# print(process(sample_input))

def blocked(x, y, sensors, beacons):
    if (x, y) in beacons:
        return False
    for sx, sy, d in sensors:
        if abs(sx - x) + abs(sy - y) <= d:
            return True
    return False

def p1(input, testrow):
    data = process(input)
    sensors = set()
    beacons = set()
    for line in data:
        sx, sy, bx, by = [int(i) for i in re.findall(r'-?\d+', line)]
        distance = abs(bx - sx) + abs(by - sy)
        sensors.add((sx, sy, distance))
        beacons.add((bx, by))

    ans = 0
    for x in range(min([x - d for x,_,d in sensors]), max([x + d for x,_,d in sensors])):
        ans += 1 if blocked(x, testrow, sensors, beacons) else 0
    return ans

def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def score(loc):
    return loc[0] * 4000000 + loc[1]

def p2(input, maxsize):
    data = process(input)
    beacons = set()
    sensors = set()
    for line in data:
        sx, sy, bx, by = [int(i) for i in re.findall(r'-?\d+', line)]
        distance = abs(bx - sx) + abs(by - sy)
        beacons.add((bx, by))
        sensors.add((sx, sy, distance))


    for sx, sy, d in sensors:
        for x in range(d+2):
            y = d - x + 1
            sw = (sx + x, sy + y)
            ne = (sx + x, sy - y)
            nw = (sx - x, sy - y)
            se = (sx - x, sy + y)
            for p in [sw, ne, nw, se]:
                if 0<=p[0]<=maxsize and 0<=p[1]<=maxsize and not blocked(p[0],p[1], sensors, beacons) and p not in sensors:
                    return score(p)
    return "Not found"

if sample_answer1:
    sample_result = p1(sample_input, 10)
    print("sample1 test", sample_result == sample_answer1)
    print("sample1", sample_result)
    if sample_result == sample_answer1:
        print("\nproblem1", p1(input, 2000000), "\n\n")

if sample_answer2:
    sample_result = p2(sample_input, 20)
    print("sample2 test", sample_result == sample_answer2)
    print("sample2", sample_result)
    if sample_result == sample_answer2:
        print("\nproblem2", p2(input, 4000000), "\n\n")


print("\ndone")
