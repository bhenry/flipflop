from collections import OrderedDict
import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""

sample_answer1 = 3068
sample_answer2 = 1514285714288

rocks = """####

 #
###
 #

  #
  #
###

#
#
#
#

##
##""".strip().split("\n\n")

class Rock():
    def __init__(self, rock):
        self.rock = "\n" + "\n".join(f"  {l}" for l in rock.replace("#", "@").splitlines()) + "\n"*4

    def __repr__(self):
        return self.rock

class Cave():
    def __init__(self, wind):
        self.wind = wind
        self._height = 0
        self.cave = "\n-------"
        self.store = OrderedDict()

    @property
    def height(self):
        return self._height + len(self.cave.splitlines()) - (1 if self.cave.splitlines()[-1] == "-------" else 0)

    def __repr__(self):
        return self.cave

    def add_rock(self, rock):
        self.cave = rock + self.cave[1:]

    def shiftl(self):
        fr = self.falling_rock()[:-1]
        newrock = []
        for l in fr:
            lpiece = l.find("@")
            rpiece = l.rfind("@")
            if lpiece == 0:
                return False
            if l[lpiece-1] == "#":
                return False
            newl = l[:lpiece-1] + l[lpiece:rpiece+1] + " " + l[rpiece+1:]
            newrock.append(newl.rstrip())
        self.cave = self.cave.replace("\n".join(fr), "\n".join(newrock))
        return True

    def shiftr(self):
        fr = self.falling_rock()[:-1]
        newrock = []
        for l in fr:
            l = l.ljust(7)
            lpiece = l.find("@")
            rpiece = l.rfind("@")
            if rpiece == 6:
                return False
            if l[rpiece+1] == "#":
                return False
            newl = l[:lpiece] + " " + l[lpiece:rpiece+1] + l[rpiece+2:]
            newrock.append(newl)
        self.cave = self.cave.replace("\n".join(fr), "\n".join(newrock))
        return True

    def falling_rock(self):
        found_rock = False
        moving_rows = []
        for l in self.cave.splitlines():
            if l.find("@") != -1:
                found_rock = True
                moving_rows.append(l)
            if found_rock and l.find("@") == -1:
                moving_rows.append(l)
                return moving_rows
        return []

    def drop(self):
        if len(self.cave.split("\n\n")) > 1:
            self.cave = self.cave.replace("\n\n", "\n", 1)
            return True
        newrocklines = []
        falling_rock = self.falling_rock() or []
        if falling_rock[0].find("#") != -1:
            newrocklines.append(falling_rock[0].replace("@", " "))
        for l, l2 in zip(falling_rock, falling_rock[1:]):
            l = l.ljust(7)
            l2 = l2.ljust(7)
            if l.find('@') != -1:
                for i in range(7):
                    if l[i] == "@" and l2[i] in ["#", "-"]:
                        return False
        for i in range(len(falling_rock)-1):
            old_above = falling_rock[i].ljust(7)
            old_line = falling_rock[i+1].ljust(7)
            newline = ""
            for t,b in zip(old_above, old_line):
                if t == "@":
                    newline += "@"
                else:
                    newline += " " if b == "@" else b
            newrocklines.append(newline.rstrip())
        self.cave = self.cave.replace("\n".join(falling_rock), "\n".join(newrocklines))
        return True

    def settle(self):
        if len(self.cave.splitlines()) > 600:
            self._height += 199 if self.cave.splitlines()[-1] == "-------" else 200
            self.cave = "\n".join(self.cave.splitlines()[:-200])
        self.cave = self.cave.replace("@", "#")

    def fill(self, n):
        cycles = 0
        for r in range(n):
            if self.height > 14:
                pass
            rock = Rock(rocks[r % len(rocks)]).rock
            self.add_rock(rock)
            while True:
                w = self.wind[cycles % len(self.wind)]
                cycles += 1
                self.shiftl() if w == "<" else self.shiftr()

                if not self.drop():
                    key = (r % len(rocks), cycles % len(self.wind), self.cave.find("@"))
                    if not self.store.get(key):
                        self.store[key] = (self.height, self.cave.splitlines()[:5] + self.cave.splitlines()[-5:], r)
                    else:
                        return (
                            (self.height, self.cave.splitlines()[:5] + self.cave.splitlines()[-5:], r),
                            self.store[key],
                        )

                    self.settle()
                    break
                pass

def process(input):
    return input.strip()

def p1(input):
    n = 2022
    wind = process(input)
    cave = Cave(wind)
    info = cave.fill(n)
    print(info)
    return ((n - info[0][2])//(info[0][2]-info[1][2]))*(info[0][0]-info[1][0]) + info[1][0] -1
    return (n//(info[0][2]-info[1][2]))*(info[0][0]-info[1][0]+1) + info[1][0]

def p2(input):
    print("this will not complete in a reasonable time")
    wind = process(input)
    cave = Cave(wind)
    info = cave.fill(1000000000000)
    print(info)
    return (1000000000000//(info[0][2]-info[1][2]))*(info[0][0]-info[1][0]) + info[1][0] - (2 if info[0][0] > 200 else 3)
    # with open(f'{path_to_day}/cave.txt', 'w+') as f: f.write(cave.cave)
    return cave.height-2

# if sample_answer1:
#     sample_result = p1(sample_input)
#     print("sample1", sample_result)
#     if sample_result == sample_answer1:
#         print("sample1 test pass")
#         print("\nproblem1", p1(input), "\n\n")

if sample_answer2:
    sample_result = p2(sample_input)
    print("sample2", sample_result)
    if sample_result == sample_answer2:
        print("sample2 test pass")
        print("\nproblem2", p2(input), "\n\n")


print("\ndone")
